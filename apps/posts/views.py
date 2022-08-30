from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied
from django.http import HttpResponseRedirect, JsonResponse
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic

from apps.posts.models import Post, Comment
from apps.posts.services.create_comment import create_comment
from apps.posts.services.create_post import create_post
from apps.posts.services.post_stat import get_posts_stat


class PostIndexView(generic.ListView):
    template_name = 'posts/index.html'
    context_object_name = 'latest_post_list'
    queryset = Post.objects.order_by('-pub_date')[:10]


class PostDetailView(generic.DetailView):
    model = Post
    template_name = 'posts/detail.html'
    slug_url_kwarg = 'id'
    slug_field = 'id'


@login_required
def create_post_view(request):
    if request.method == 'POST':
        create_post(request.POST, request.user)
        return HttpResponseRedirect(reverse('posts:post_index'))

    return render(request, 'posts/create.html')


@login_required
def delete_post_view(request, id):
    if request.method == 'POST':
        post = get_object_or_404(Post, id=id)
        if post.author == request.user or request.user.is_superuser:
            post.delete()
            return HttpResponseRedirect(reverse('posts:post_index'))
        raise PermissionDenied()


def posts_stat_view(request):
    return JsonResponse(get_posts_stat())


@login_required
def post_add_comment_view(request, id):
    data = {
        'text': request.POST.get('comment_text'),
        'post': id,
    }
    create_comment(data, request.user)

    return HttpResponseRedirect(reverse('posts:post_detail', args=(id,)))


@login_required
def delete_comment_view(request, id):
    if request.method == 'POST':
        comment = get_object_or_404(Comment, id=id)
        if comment.author == request.user or request.user.is_superuser:
            post_id = comment.post.id
            comment.delete()
            return HttpResponseRedirect(reverse('posts:post_detail', args=(post_id,)))
        raise PermissionDenied()