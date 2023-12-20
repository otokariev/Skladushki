from django.http import HttpResponse, JsonResponse
from django.contrib.auth.models import User
from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.core.exceptions import ObjectDoesNotExist

from rest_framework import generics, viewsets, status
from rest_framework.authentication import TokenAuthentication
from rest_framework.generics import ListAPIView
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view

from .models import Account, About, Contacts
from .permissions import IsAdminOrReadOnly, IsOwnerOrReadOnly
from .serializers import AccountSerializer, AboutSerializer, ContactsSerializer


# @api_view(['GET', ])
# def api_detail_account_view(request, slug):  #!FIXME add slug into model
#
#     try:
#         account = Account.objects.get(slug=slug)
#     except ObjectDoesNotExist:  #!FIXME check the exception
#         return Response(status=status.HTTP_404_NOT_FOUND)
#
#     if request.method == 'GET':
#         serializer = AccountSerializer(account)
#         return Response(serializer.data)


class UserAPIListPagination(PageNumberPagination):
    page_size = 3
    page_size_query_param = 'page_size'
    max_page_size = 1000


# class UserView(APIView):
#
#     def get_user(self, pk):
#         return get_object_or_404(UserModel, user_pk=pk)
#
#     def get(self, request, pk=None):
#         if pk:
#             user = self.get_user(pk)
#             serializer = UserSerializer(user)
#         else:
#             users = UserModel.objects.all()
#             serializer = UserSerializer(users, many=True)
#         return Response(serializer.data)
#
#     def post(self, request):
#         serializer = UserSerializer(data=request.data)
#
#         if serializer.is_valid():
#             serializer.save()
#             return Response("Student Created Successfully", status=status.HTTP_201_CREATED)
#         return Response("Failed to Add Student", status=status.HTTP_400_BAD_REQUEST)
#
#     def put(self, request, pk=None):
#         user_to_update = self.get_user(pk)
#         serializer = UserSerializer(instance=user_to_update, data=request.data, partial=True)
#
#         if serializer.is_valid():
#             serializer.save()
#             return Response("Student Updated Successfully")
#         return Response("Failed to Update Student", status=status.HTTP_400_BAD_REQUEST)
#
#     def delete(self, request, pk=None):
#         user_to_delete = self.get_user(pk)
#         user_to_delete.delete()
#         return Response("Student Deleted Successfully", status=status.HTTP_204_NO_CONTENT)


class AccountAPIList(generics.ListCreateAPIView):
    queryset = Account.objects.all()
    serializer_class = AccountSerializer
    # permission_classes = (IsAuthenticatedOrReadOnly, )
    pagination_class = UserAPIListPagination


class AccountAPIUpdate(generics.RetrieveUpdateAPIView):
    queryset = Account.objects.all()
    serializer_class = AccountSerializer
    permission_classes = (IsOwnerOrReadOnly, )
    # authentication_classes = (TokenAuthentication, )


# class AccountAPIDestroy(generics.RetrieveDestroyAPIView):
#     queryset = Account.objects.all()
#     serializer_class = AccountSerializer
#     permission_classes = (IsAdminOrReadOnly, )


class AboutAPIView(ListAPIView):
    queryset = About.objects.all()
    serializer_class = AboutSerializer


class ContactsAPIView(ListAPIView):
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
