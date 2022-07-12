from django.http import HttpResponse


def index(request):
    return HttpResponse('Главная страница')


def groups(request):
    return HttpResponse('Страницы сообществ')


def group_posts(request, slug):
    return HttpResponse(f'Страница сообщества {slug}')
