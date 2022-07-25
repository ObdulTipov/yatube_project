from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    template = 'posts/index.html'
    title = 'Последние обновления на сайте'
    context = {
        'title': title,
        'text': 'Это главная страница проекта Yatube'
    }
    return render(request, template, context)


def groups(request):
    return HttpResponse('Страницы сообществ')


# В урл мы ждем парметр, и нужно его прередать в функцию для использования
def group_posts(request, slug):
    template = 'posts/group_list.html'
    title = 'Лев Толстой – зеркало русской революции.'
    context = {
        'title': title,
        'text': 'Здесь будет информация о группах проекта Yatube'
    }
    return render(request, template, context)
