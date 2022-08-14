from django.urls import path
from django.contrib.auth import views as django_views

from . import views

app_name = 'accounts'

urlpatterns = [
    path(
        'login/',
        django_views.LoginView.as_view(
            template_name='accounts/login.html'
        ),
        name='login',
    ),
    path(
        'logout/',
        django_views.LogoutView.as_view(
            template_name='accounts/logout.html'
        ),
        name='logout',
    ),
    path(
        'profile/',
        views.ProfileView.as_view(),
        name='profile',
    )
]
