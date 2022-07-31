from django.urls import path

from . import views

app_name = 'posts'

urlpatterns = [
    path('', views.PostIndexView.as_view(), name='post_index'),
    path('create/', views.create_post, name="post_create"),
    path('<int:pk>/', views.PostDetailView.as_view(), name="post_detail"),
    path('<int:pk>/delete/', views.delete_post, name="post_delete"),
    path('<int:pk>/comments/create/', views.post_add_comment, name="post_add_comment"),
    path('comments/<int:pk>/delete/', views.delete_comment, name="comment_delete"),
]

