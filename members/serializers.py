from rest_framework import serializers
from .models import Member


class MemberSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Member
        fields = '__all__'
