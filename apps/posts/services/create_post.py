from django.contrib.auth import get_user_model
from django.utils import timezone

from apps.posts.models import Post

User = get_user_model()


def create_post(data: dict, user: User) -> Post:
    """Создать пост."""
    return Post.objects.create(
        title=data.get('title'),
        text=data.get('text'),
        pub_date=timezone.now(),
        author=user,
    )
