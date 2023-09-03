from django.urls import path, include
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.login_view, name='login'),
    path('main', views.login_sucess, name='main'),
    path('logout', views.logout_view, name='logout'),
]