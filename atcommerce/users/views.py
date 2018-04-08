from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from rest_framework import viewsets, serializers
from rest_framework.response import Response


"""
/v1/users/profile

This should use a model which is an extension of
the Django User's model. Providing a user profile
which tells information about number of uploaded files.

It should _only_ display the currently logged in user's profile,
if the user is not an admin, otherwise we should allowe the admin,
to check the status on other users, as well as update those users.
"""

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'email', 'first_name', 'is_staff', 'last_login')


class UserViewSet(viewsets.ModelViewSet):
    """
    Gets the currently logged in user.
    Users are logged in at `auth/login`
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def list(self, request):
        queryset = User.objects.get(id=request.user.id)
        serializer = UserSerializer(queryset)
        return Response(serializer.data)
