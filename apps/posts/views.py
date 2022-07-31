from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.views import generic
from django.urls import reverse
from django.utils import timezone

from apps.posts.models import Post, Comment


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
        Post.objects.create(title=title, text=text, pub_date=timezone.now())
        return HttpResponseRedirect(reverse('posts:post_index'))
    return render(request, 'posts/create.html')


def post_add_comment(request, pk):
    post = get_object_or_404(Post, pk=pk)
    comment_text = request.POST['comment_text']
    Comment.objects.create(text=comment_text, post=post, pub_date=timezone.now())
    return HttpResponseRedirect(reverse('posts:post_detail', args=(pk,)))

