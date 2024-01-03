from django.contrib.auth import authenticate
from django.shortcuts import get_object_or_404
from drf_spectacular.types import OpenApiTypes

from rest_framework import status, generics
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import UpdateModelMixin
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticated
from rest_framework.generics import UpdateAPIView
from rest_framework.authentication import TokenAuthentication
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.authtoken.models import Token
from rest_framework.filters import SearchFilter, OrderingFilter

from drf_spectacular.utils import extend_schema, OpenApiParameter, OpenApiExample

from .models import Account, About, Contacts
from .serializers import (
    RegistrationSerializer,
    AccountProfileSerializer,
    UpdateAccountProfileSerializer,
    ChangePasswordSerializer,
    LoginAuthTokenSerializer,
    CheckAccountIfExistSerializer,
    AboutSerializer,
    ContactsSerializer,
    SearchSerializer,
)


class UserAPIListPagination(PageNumberPagination):
    page_size = 3
    page_size_query_param = 'page_size'
    max_page_size = 1000


# Register
# Response: https://gist.github.com/mitchtabian/c13c41fa0f51b304d7638b7bac7cb694
# Url: https://<your-domain>/api/account/register
@extend_schema(
    responses=RegistrationSerializer,
    request=OpenApiTypes.OBJECT,
    description="Credentials for authentication",
    parameters=None,
    examples=[OpenApiExample(
        name="Example",
        value={
            "email": "user@example.com",
            "password": "password",
            "password2": "password",
            "first_name": "Nameless",
            "last_name": "User",
            "sex": "1",
            "city": "NY",
            "phone": "1(23)-456-789-0",
            "bio": "My name is...",
            "photo": "http://img2.wikia.nocookie.net/__cb20140427211725/dragcave/images/6/6e/No_avatar.jpg"
        })
    ]
)
@api_view(['POST', ])
@permission_classes([])
@authentication_classes([])
def registration_view(request):
    if request.method == 'POST':
        data = {}
        email = request.data.get('email').lower()
        if validate_email(email) is not None:
            data['error_message'] = 'That email is already in use.'
            data['response'] = 'Error'
            return Response(data)

        # username = request.data.get('username')
        # if validate_username(username) is not None:
        #     data['error_message'] = 'That username is already in use.'
        #     data['response'] = 'Error'
        #     return Response(data)

        serializer = RegistrationSerializer(data=request.data)

        if serializer.is_valid():
            account = serializer.save()
            data['response'] = 'successfully registered new user.'
            data['email'] = account.email
            # data['username'] = account.username
            data['pk'] = account.pk
            token = Token.objects.get(user=account).key
            data['token'] = token
        else:
            data = serializer.errors
        return Response(data)


def validate_email(email):
    account = None
    try:
        account = Account.objects.get(email=email)
    except Account.DoesNotExist:
        return None
    if account is not None:
        return email


# def validate_username(username):
#     account = None
#     try:
#         account = Account.objects.get(username=username)
#     except Account.DoesNotExist:
#         return None
#     if account is not None:
#         return username


# Account properties
# Response: https://gist.github.com/mitchtabian/4adaaaabc767df73c5001a44b4828ca5
# Url: https://<your-domain>/api/account/
# Headers: Authorization: Token <token>
@extend_schema(responses=AccountProfileSerializer)
@api_view(['GET', ])
# @permission_classes((IsAuthenticated,))
@permission_classes([])
@authentication_classes([])
def account_profile_id_view(request, profile_id):
    account = get_object_or_404(Account, pk=profile_id)

    if request.method == 'GET':
        serializer = AccountProfileSerializer(account)
        return Response(serializer.data)


@extend_schema(responses=AccountProfileSerializer)
@api_view(['GET', ])
# @permission_classes((IsAuthenticated,))
@permission_classes([])
@authentication_classes([])
def account_profile_view(request):
    try:
        accounts = Account.objects.all()
    except Account.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = AccountProfileSerializer(accounts, many=True)
        return Response(serializer.data)


# Account update properties
# Response: https://gist.github.com/mitchtabian/72bb4c4811199b1d303eb2d71ec932b2
# Url: https://<your-domain>/api/account/properties/update
# Headers: Authorization: Token <token>
@extend_schema(
    responses=UpdateAccountProfileSerializer,
    request=OpenApiTypes.OBJECT,
    description="Credentials for authentication",
    parameters=None,
    examples=[OpenApiExample(
        name="Example",
        value={
            "email": "user@example.com",
            "password": "password",
            "password2": "password",
            "first_name": "Nameless",
            "last_name": "User",
            "sex": "1",
            "city": "NY",
            "phone": "1(23)-456-789-0",
            "bio": "My name is...",
            "photo": "http://img2.wikia.nocookie.net/__cb20140427211725/dragcave/images/6/6e/No_avatar.jpg"
        })
    ]
)
@api_view(['PUT', ])
@permission_classes((IsAuthenticated,))
def update_account_profile_view(request):
    try:
        account = request.user
    except Account.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'PUT':
        serializer = UpdateAccountProfileSerializer(account, data=request.data)
        data = {}
        if serializer.is_valid():
            serializer.save()
            data['response'] = 'Account update success'
            return Response(data=data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# LOGIN
# Response: https://gist.github.com/mitchtabian/8e1bde81b3be342853ddfcc45ec0df8a
# URL: http://127.0.0.1:8000/api/account/login
class LoginAuthTokenView(APIView):
    authentication_classes = []
    permission_classes = []

    @extend_schema(
        responses=LoginAuthTokenSerializer,
        request=OpenApiTypes.OBJECT,
        description="Credentials for authentication",
        parameters=None,
        examples=[OpenApiExample(
            name="Example",
            value={
                "email": "user@example.com",
                "password": "password",
            })
        ]
    )
    def post(self, request):
        context = {}

        # email = request.POST.get('email')
        # password = request.POST.get('password')

        data = request.data
        email = data.get('email')
        password = data.get('password')

        account = authenticate(email=email, password=password)
        if account:
            try:
                token = Token.objects.get(user=account)
            except Token.DoesNotExist:
                token = Token.objects.create(user=account)
            context['response'] = 'Successfully authenticated.'
            context['pk'] = account.pk
            context['email'] = email.lower()
            context['token'] = token.key
        else:
            context['response'] = 'Error'
            context['error_message'] = 'Invalid credentials'

        return Response(context)


# @extend_schema(request=CheckAccountIfExistSerializer, parameters=[{'name': 'email'}])
# @extend_schema(responses=CheckAccountIfExistSerializer)
@extend_schema(
    request=CheckAccountIfExistSerializer,
    parameters=[
        OpenApiParameter(name='email', location=OpenApiParameter.QUERY, type=str),
    ]
)
@api_view(['GET', ])
@permission_classes([])
@authentication_classes([])
def check_if_account_exists(request):
    if request.method == 'GET':
        email = request.GET.get('email', '').lower()
        data = {}

        if email:
            try:
                account = Account.objects.get(email=email)
                data['response'] = "Account exist"
                data['email'] = email
            except Account.DoesNotExist:
                data['response'] = "Account does not exist"
        else:
            data['response'] = "Email parameter missing"

        return Response(data)


@extend_schema(
    responses=ChangePasswordSerializer,
    request=OpenApiTypes.OBJECT,
    description="Credentials for authentication",
    parameters=None,
    examples=[OpenApiExample(
        name="Example",
        value={
            "old_password": "password",
            "new_password": "new_password",
            "confirm_new_password": "new_password",
        })
    ]
)
class ChangePasswordView(APIView):
    serializer_class = ChangePasswordSerializer
    model = Account
    permission_classes = (IsAuthenticated,)
    authentication_classes = (TokenAuthentication,)

    def get_object(self, queryset=None):
        obj = self.request.user
        return obj

    def put(self, request, *args, **kwargs):
        self.object = self.get_object()
        serializer = self.get_serializer(data=request.data)

        if serializer.is_valid():
            # Check old password
            if not self.object.check_password(serializer.data.get("old_password")):
                return Response({"old_password": ["Wrong password."]}, status=status.HTTP_400_BAD_REQUEST)

            # confirm the new passwords match
            new_password = serializer.data.get("new_password")
            confirm_new_password = serializer.data.get("confirm_new_password")
            if new_password != confirm_new_password:
                return Response({"new_password": ["New passwords must match"]}, status=status.HTTP_400_BAD_REQUEST)

            # set_password also hashes the password that the user will get
            self.object.set_password(serializer.data.get("new_password"))
            self.object.save()
            return Response({"response": "successfully changed password"}, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@permission_classes([])
@authentication_classes([])
@extend_schema(responses=AboutSerializer)
class AboutAPIView(APIView):
    def get(self, request, *args, **kwargs):
        queryset = Contacts.objects.all()
        serializer = ContactsSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


@extend_schema(responses=ContactsSerializer)
class ContactsAPIView(APIView):
    def get(self, request, *args, **kwargs):
        queryset = Contacts.objects.all()
        serializer = ContactsSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


@extend_schema(responses=SearchSerializer)
class SearchAPIView(generics.ListAPIView):
    queryset = Account.objects.all()
    serializer_class = SearchSerializer
    filter_backends = [SearchFilter]
    search_fields = [
        'email',
        'first_name',
        'last_name',
        'phone',
        'city',
        'bio',
    ]
