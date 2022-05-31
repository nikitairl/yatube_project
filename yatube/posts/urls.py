from django.urls import path
from . import views

urlpatterns = [
    # Главная страница
    path('', views.index),
    path('group/<slug>/', views.group_posts),
]
