from django.http import HttpResponse
from rest_framework import generics, viewsets
from django.shortcuts import render
from rest_framework.authentication import TokenAuthentication
from rest_framework.generics import ListAPIView
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from .models import UserProfile, About, Contacts
from .permissions import IsAdminOrReadOnly, IsOwnerOrReadOnly
from .serializers import UserSerializer, AboutSerializer, ContactsSerializer


class UserAPIListPagination(PageNumberPagination):
    page_size = 3
    page_size_query_param = 'page_size'
    max_page_size = 2


class UserAPIList(generics.ListCreateAPIView):
    queryset = UserProfile.objects.all()
    serializer_class = UserSerializer
    permission_classes = (IsAuthenticatedOrReadOnly, )
    pagination_class = UserAPIListPagination


class UserAPIUpdate(generics.RetrieveUpdateAPIView):
    queryset = UserProfile.objects.all()
    serializer_class = UserSerializer
    permission_classes = (IsOwnerOrReadOnly, )
    # authentication_classes = (TokenAuthentication, )


class UserAPIDestroy(generics.RetrieveDestroyAPIView):
    queryset = UserProfile.objects.all()
    serializer_class = UserSerializer
    permission_classes = (IsAdminOrReadOnly, )


class AboutView(ListAPIView):
    queryset = About.objects.all()
    serializer_class = AboutSerializer


class ContactsView(ListAPIView):
    queryset = Contacts.objects.all()
    serializer_class = ContactsSerializer


def profile(request):  # main page when authorized
    return HttpResponse('Профиль пользователя')


def search(request):  # main page when unregistered or unauthorized
    return HttpResponse('Поиск')


def register(request):
    return HttpResponse('Регистрация')


def login(request):
    return HttpResponse('Логин')
