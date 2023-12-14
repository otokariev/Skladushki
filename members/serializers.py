from rest_framework import serializers
from .models import Member, About, Contacts


class MemberSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Member
        fields = '__all__'


class AboutSerializer(serializers.ModelSerializer):

    class Meta:
        model = About
        fields = '__all__'


class ContactsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Contacts
        fields = '__all__'
