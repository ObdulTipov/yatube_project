from django.urls import path

from . import views

urlpatterns = [
    # Главная страница
    path('', views.index),
    # Страница сообщества
    path('group/', views.groups),
    # Страница сообщества {slug}. Ждем пременную типа slug,
    # и будем использовать ее под именем slug
    path('group/<slug:slug>/', views.group_posts),
]
