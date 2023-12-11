from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render


def index(request):
    return render(request, 'members/index.html')


def about(request):
    return HttpResponse('Информация о сайте')


def contacts(request):
    return HttpResponse('Телефон, почта, соц.сети')


def register(request):
    return HttpResponse('Форма заполнения анкеты')


def login(request):
    return HttpResponse('Форма входа на сайт')


def forgot_password(request):
    return HttpResponse('Форма смены пароля')


def categories(request, categories_id):
    return HttpResponse(f'<h1>Категории</h1><p>id = {categories_id}</p>')


def categories_by_slug(request, categories_slug):
    return HttpResponse(f'<h1>Категории</h1><p>slug = {categories_slug}</p>')


def page_not_found(request, exception):
    return HttpResponseNotFound('<h2>Страница не найдена</h2>')
