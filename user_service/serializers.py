from rest_framework import serializers
from .models import User, Role


class UserSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = User
        fields = ('url', 'id', 'first_name', 'last_name', 'email', 'role', 'created_at', 'updated_at',)


class RoleSerializer(serializers.ModelSerializer):

    class Meta:
        model = Role
        fields = ('url', 'id', 'role_name', 'created_at', 'updated_at',)
