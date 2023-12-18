from rest_framework import serializers
from .models import UserModel, UserProfile, About, Contacts


class UserSerializer(serializers.ModelSerializer):
    # user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = UserModel
        fields = ['first_name', 'last_name', 'username', 'email', 'password']


class AboutSerializer(serializers.ModelSerializer):

    class Meta:
        model = About
        fields = '__all__'


class ContactsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Contacts
        fields = '__all__'
