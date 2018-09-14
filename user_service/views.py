from django.db.models import ProtectedError
from rest_framework import viewsets
from rest_framework.response import Response
from .models import User, Role, LeadSource
from .serializers import UserSerializer, RoleSerializer, LeadSourceSerializer


class UserView(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class RoleView(viewsets.ModelViewSet):
    queryset = Role.objects.all()
    serializer_class = RoleSerializer

    def destroy(self, request, pk=None):
        queryset = Role.objects.filter(role_name=self.get_object()).first().users.first()
        if not queryset:
            self.perform_destroy(self.get_object())
            return Response({'status': 'ok', 'description': 'role deleted.'})
        else:
            return Response({'status': 'error', 'description': 'role is not empty.'})


class LeadSourceView(viewsets.ModelViewSet):
    queryset = LeadSource.objects.all()
    serializer_class = LeadSourceSerializer

    def destroy(self, request, pk=None):
        try:
            self.perform_destroy(self.get_object())
        except ProtectedError:
            return Response({'status': 'error', 'description': 'lead source is not empty.'})
        else:
            return Response({'status': 'ok', 'description': 'lead source deleted.'})
