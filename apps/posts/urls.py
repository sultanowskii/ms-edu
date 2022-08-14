from django.urls import path

from . import views

app_name = 'posts'

urlpatterns = [
    path('', views.PostIndexView.as_view(), name='index'),
    path('create/', views.create_post, name='create'),
    path('<int:pk>/', views.PostDetailView.as_view(), name='detail'),
    path('<int:pk>/delete/', views.delete_post, name='delete'),
    path('stat/', views.posts_stat, name='stat'),
    path('<int:pk>/comments/create/', views.post_add_comment, name='add_comment'),
    path('comments/<int:pk>/delete/', views.delete_comment, name='delete_comment'),
]

