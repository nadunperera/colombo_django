from rest_framework import viewsets
from .models import User, Role, LeadSource
from .serializers import UserSerializer, RoleSerializer, LeadSourceSerializer


class UserView(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class RoleView(viewsets.ModelViewSet):
    queryset = Role.objects.all()
    serializer_class = RoleSerializer

    def perform_destroy(self, instance):
        queryset = Role.objects.filter(role_name=instance).first().users.first()
        if not queryset:
            print('Ok you can delete!')
        else:
            print('You cannot delete for shit!')


class LeadSourceView(viewsets.ModelViewSet):
    queryset = LeadSource.objects.all()
    serializer_class = LeadSourceSerializer
