from rest_framework import serializers
from .models import Account, About, Contacts


class RegistrationSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(style={'input_type': 'password'}, write_only=True)
    photo = serializers.URLField()

    class Meta:
        model = Account
        fields = [
            'email',
            'password',
            'password2',
            'first_name',
            'last_name',
            'sex',
            'city',
            'phone',
            'bio',
            'photo',
        ]
        extra_kwargs = {
            'password': {'write_only': True},
        }

    def save(self):
        account = Account(
            email=self.validated_data['email'],
            first_name=self.validated_data.get('first_name', ''),
            last_name=self.validated_data.get('last_name', ''),
            sex=self.validated_data.get('sex', ''),
            city=self.validated_data.get('city', ''),
            phone=self.validated_data.get('phone', ''),
            bio=self.validated_data.get('bio', ''),
            photo=self.validated_data.get('photo', ''),
        )

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
        extra_kwargs = {
            'password': {'write_only': True},
        }


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
