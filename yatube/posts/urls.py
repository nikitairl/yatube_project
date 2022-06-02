# from django.urls import path
# from . import views

# urlpatterns = [
#     # Главная страница
#     path('', views.index, name='index'),
#     path('group/<slug:slug>/', views.group_posts, name='group_posts'),
# ]


from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('group/<slug:slug>', views.group_posts, name='group'),
]