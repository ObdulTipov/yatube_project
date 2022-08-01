from django.shortcuts import render, get_object_or_404
from .models import LAST_TEN_POSTS, Post, Group


def index(request):
    posts = Post.objects.all()[:LAST_TEN_POSTS]
    title = 'Главная страница Yatube'
    text = 'Последние обновления на сайте'
    context = {
        'title': title,
        'text': text,
        'posts': posts,
    }
    return render(request, 'posts/index.html', context)


def group_posts(request, slug):
    group = get_object_or_404(Group, slug=slug)
    posts = Post.objects.select_related('group')[:LAST_TEN_POSTS]
    context = {
        'group': group,
        'posts': posts,
    }
    return render(request, 'posts/group_list.html', context)
