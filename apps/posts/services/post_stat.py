from django.db.models import Max, Min, Avg, Count

from apps.posts.models import Post


def get_posts_stat() -> dict:
    """Получить стастику по постам."""
    post_count = Post.objects.count()

    comment_summary = (
        Post.objects
        .annotate(comment_count=Count('comments'))
        .aggregate(
            min_comment_cnt=Min('comment_count'),
            max_comment_cnt=Max('comment_count'),
            avg_comment_cnt=Avg('comment_count'),
        )
    )
    min_comment_cnt = comment_summary['min_comment_cnt']
    max_comment_cnt = comment_summary['max_comment_cnt']
    avg_comment_cnt = comment_summary['avg_comment_cnt']

    post_with_many_comments = (
        Post.objects
        .annotate(comment_count=Count('comments'))
        .filter(comment_count__gte=avg_comment_cnt)
        .count()
    )

    return dict(
        post_count=post_count,
        min_comment_cnt=min_comment_cnt,
        max_comment_cnt=max_comment_cnt,
        avg_comment_cnt=avg_comment_cnt,
        post_with_many_comments=post_with_many_comments,
    )
