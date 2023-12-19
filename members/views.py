from django.http import HttpResponse, JsonResponse
from rest_framework import generics, viewsets, status
from django.shortcuts import render
from rest_framework.authentication import TokenAuthentication
from rest_framework.generics import ListAPIView
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404
from .models import UserModel, UserProfile, About, Contacts
from .permissions import IsAdminOrReadOnly, IsOwnerOrReadOnly
from .serializers import UserModelSerializer, AboutSerializer, ContactsSerializer
from django.contrib.auth.models import User


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


class UserModelAPIList(generics.ListCreateAPIView):
    queryset = UserModel.objects.all()
    serializer_class = UserModelSerializer
    # permission_classes = (IsAuthenticatedOrReadOnly, )
    pagination_class = UserAPIListPagination


class UserModelAPIUpdate(generics.RetrieveUpdateAPIView):
    queryset = UserModel.objects.all()
    serializer_class = UserModelSerializer
    permission_classes = (IsOwnerOrReadOnly, )
    # authentication_classes = (TokenAuthentication, )


# class UserModelAPIDestroy(generics.RetrieveDestroyAPIView):
#     queryset = UserModel.objects.all()
#     serializer_class = UserModelSerializer
#     permission_classes = (IsAdminOrReadOnly, )


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
