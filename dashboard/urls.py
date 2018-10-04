from django.urls import path
from . import views

urlpatterns = [
    path('dashboard/', views.all_user, name='all_user'),
    path('profile/<str:firstname>-<str:lastname>', views.profile, name='profile'),
]