from django.http import HttpResponseRedirect, JsonResponse
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.utils import timezone
from django.views import generic

from apps.posts.models import Post, Comment
from apps.posts.services.post_stat import get_posts_stat


class PostIndexView(generic.ListView):
    template_name = 'posts/index.html'
    context_object_name = 'latest_post_list'

    def get_queryset(self):
        """Return the last five published posts."""
        return Post.objects.order_by('-pub_date')[:5]


class PostDetailView(generic.DetailView):
    model = Post
    template_name = 'posts/detail.html'


def create_post(request):
    if request.method == 'POST':
        title = request.POST['title']
        text = request.POST['text']

        Post.objects.create(
            title=title,
            text=text,
            pub_date=timezone.now(),
        )

        return HttpResponseRedirect(reverse('posts:post_index'))

    return render(request, 'posts/create.html')


def delete_post(request, pk):
    if request.method == 'POST':
        post = get_object_or_404(Post, pk=pk)
        post.delete()
        return HttpResponseRedirect(reverse('posts:post_index'))


def posts_stat(request):
    return JsonResponse(get_posts_stat())
    

def post_add_comment(request, pk):
    post = get_object_or_404(Post, pk=pk)
    comment_text = request.POST['comment_text']
    Comment.objects.create(text=comment_text, post=post, pub_date=timezone.now())
    return HttpResponseRedirect(reverse('posts:post_detail', args=(pk,)))


def delete_comment(request, pk):
    if request.method == 'POST':
        comment = get_object_or_404(Comment, pk=pk)
        post_pk = comment.post.pk
        comment.delete()
        return HttpResponseRedirect(reverse('posts:post_detail', args=(post_pk,)))
