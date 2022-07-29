from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
# Импортируем модель, чтобы обратиться к ней
from .models import Post, Group

def index(request):
    posts = Post.objects.order_by('-pub_date')[:10]
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
    posts = Post.object.filter(group=group).order_by('-pub_date')[:10]
    title = 'Лев Толстой – зеркало русской революции.'
    text = 'Здесь будет информация о группах проекта Yatube'
    context = {
        'title': title,
        'text': text,
        'group': group,
        'posts': posts,
    }
    return render(request, 'posts/group_list.html', context)
