from django.http import HttpResponse
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
