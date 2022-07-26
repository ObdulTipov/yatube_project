from django.urls import path

from . import views

app_name = 'posts'

urlpatterns = [
    # Главная страница
    path('posts/', views.index, name='posts_list'),
    # Страница сообщества
    path('group/', views.group_list, name='group_list'),
    # Страница сообщества {slug}. Ждем пременную типа slug,
    # и будем использовать ее под именем slug
    path('group/<slug:slug>/', views.group_posts_list, name='group_posts_list'),
]
