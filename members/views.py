from django.http import HttpResponse
from rest_framework import generics
from django.shortcuts import render
from rest_framework.authentication import TokenAuthentication
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from .models import Member
from .permissions import IsAdminOrReadOnly, IsOwnerOrReadOnly
from .serializers import MemberSerializer


class MemberAPIListPagination(PageNumberPagination):
    page_size = 3
    page_size_query_param = 'page_size'
    max_page_size = 2


class MemberAPIList(generics.ListCreateAPIView):
    queryset = Member.objects.all()
    serializer_class = MemberSerializer
    permission_classes = (IsAuthenticatedOrReadOnly, )
    pagination_class = MemberAPIListPagination


class MemberAPIUpdate(generics.RetrieveUpdateAPIView):
    queryset = Member.objects.all()
    serializer_class = MemberSerializer
    permission_classes = (IsOwnerOrReadOnly, )
    # authentication_classes = (TokenAuthentication, )


class MemberAPIDestroy(generics.RetrieveDestroyAPIView):
    queryset = Member.objects.all()
    serializer_class = MemberSerializer
    permission_classes = (IsAdminOrReadOnly, )


def index(request):
    return HttpResponse('Главная страница')


def about(request):
    return HttpResponse('О сайте')


def contacts(request):
    return HttpResponse('Контакты')


def register(request):
    return HttpResponse('Регистрация')


def login(request):
    return HttpResponse('Логин')
