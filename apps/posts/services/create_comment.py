from django.contrib.auth import get_user_model
from django.utils import timezone

from apps.posts.models import Comment

User = get_user_model()


def create_comment(data: dict, user: User) -> Comment:
    """Создать комментарий."""
    return Comment.objects.create(
        post_id=data.get('post'),
        text=data.get('text'),
        pub_date=timezone.now(),
        author=user,
    )
