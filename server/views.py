from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render
from oauth2_provider.views import ProtectedResourceView
from rest_framework import serializers, permissions
from rest_framework.response import Response
from rest_framework.views import APIView


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

class UserData(APIView):

    permission_classes = (permissions.IsAuthenticated,)

    def get(self, request, *args, **kwargs):
        serializer = UserSerializer(request.user)
        return Response(serializer.data)