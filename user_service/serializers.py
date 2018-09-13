from rest_framework import serializers
from .models import User, Role, LeadSource


class UserSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = User
        fields = ('url', 'id', 'first_name', 'last_name', 'age', 'email', 'role', 'lead_source', 'created_at', 'updated_at',)


class RoleSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Role
        fields = ('url', 'id', 'role_name', 'users', 'created_at', 'updated_at',)


class LeadSourceSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = LeadSource
        fields = ('url', 'id', 'source_name', 'users', 'created_at', 'updated_at')
