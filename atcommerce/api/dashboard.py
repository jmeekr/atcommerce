from django.shortcuts import get_object_or_404
from rest_framework import viewsets, serializers
from rest_framework.response import Response
from .models import Eorders

class DashboardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Eorders
        fields = ()

class DashboardViewSet(viewsets.ModelViewSet):
    """
    Gets the currently logged in user.
    Users are logged in at `auth/login`
    """
    queryset = Eorders.objects.all()
    serializer_class = DashboardSerializer

    def list(self, request):
        queryset = Eorders.objects.all()
        serializer = DashboardSerializer(queryset)
        return Response(serializer.data)

