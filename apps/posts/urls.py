from django.urls import path

from . import views

app_name = 'posts'

urlpatterns = [
    path('', views.PostIndexView.as_view(), name='post_index'),
    path('create/', views.create_post_view, name='post_create'),
    path('<int:id>/', views.PostDetailView.as_view(), name='post_detail'),
    path('<int:id>/delete/', views.delete_post_view, name='post_delete'),
    path('stat/', views.posts_stat_view, name='post_stat'),
    path('<int:id>/comments/create/', views.post_add_comment_view, name='post_add_comment'),
    path('comments/<int:id>/delete/', views.delete_comment_view, name='comment_delete'),
]

