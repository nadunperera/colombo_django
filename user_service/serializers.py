from rest_framework import serializers
from .models import User, Role, LeadSource


class UserSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = User
        fields = ('url', 'id', 'first_name', 'last_name', 'age', 'email', 'role', 'lead_source', 'mobile_number', 'office_number', 'address', 'address', 'city', 'post_code', 'purchasing_entity', 'can_not_contact', 'personal_income', 'partners_income', 'owned_properties', 'own_home', 'gst_registered', 'company_name', 'abn', 'australian_resident', 'firb_required', 'investment_needed', 'created_at', 'updated_at',)


class RoleSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Role
        fields = ('url', 'id', 'users', 'created_at', 'updated_at',)


class LeadSourceSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = LeadSource
        fields = ('url', 'id', 'source_name', 'users', 'created_at', 'updated_at')
