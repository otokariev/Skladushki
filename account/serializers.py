from rest_framework import serializers
from .models import Account, About, Contacts


class RegistrationSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(style={'input_type': 'password'}, write_only=True)

    class Meta:
        model = Account
        fields = ['email', 'password', 'password2']
        extra_kwargs = {
            'password': {'write_only': True},
        }

    def save(self):
        account = Account(email=self.validated_data['email'])

        password = self.validated_data['password']
        password2 = self.validated_data['password2']
        if password != password2:
            raise serializers.ValidationError({'password': 'Passwords must match.'})
        account.set_password(password)
        account.save()
        return account


class AccountProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = [
            'pk',
            'email',
            'first_name',
            'last_name',
            'date_joined',
            'last_login',
            'phone',
            'city',
            'bio',
            'photo',
            'sex',
        ]


class UpdateAccountProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = [
            'pk',
            'email',
            'first_name',
            'last_name',
            'phone',
            'city',
            'bio',
            'photo',
            'sex',
        ]


class LoginAuthTokenSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = [
            'pk',
            'email',
            'password',
        ]


class CheckAccountIfExistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = [
            'email',
        ]


class ChangePasswordSerializer(serializers.Serializer):
    old_password = serializers.CharField(required=True)
    new_password = serializers.CharField(required=True)
    confirm_new_password = serializers.CharField(required=True)


class AboutSerializer(serializers.ModelSerializer):
    class Meta:
        model = About
        fields = [
            'id',
            'title',
            'text',
        ]


class ContactsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contacts
        fields = [
            'id',
            'title',
            'phone',
            'email',
        ]
