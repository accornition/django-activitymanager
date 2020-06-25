from rest_framework import generics, permissions, status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import BasicAuthentication, SessionAuthentication
from .serializers import ActivitySerializer

from apps.accounts.models import User

from .models import ActivityPeriod

#from knox.auth import TokenAuthentication
from rest_framework.authentication import BasicAuthentication, SessionAuthentication, TokenAuthentication

from django.shortcuts import render

class AdminAuthenticationPermission(permissions.BasePermission):
    ADMIN_ONLY_AUTH_CLASSES = [BasicAuthentication, SessionAuthentication]

    def has_permission(self, request, view):
        user = request.user
        if user and user.is_authenticated:
            return user.is_superuser or \
                not any(isinstance(request._authenticator, x) for x in self.ADMIN_ONLY_AUTH_CLASSES) 
        return False

class ActivityList(APIView):
    authentication_classes = [BasicAuthentication, SessionAuthentication]
    permission_classes = [IsAuthenticated, AdminAuthenticationPermission]

    def get(self, request, user_id=None, format=None):
        context = {}
        if user_id is None:
            queryset = ActivityPeriod.objects.all()
            serializer = ActivitySerializer(queryset, many=True)
            context['user'] = False
        else:
            queryset = ActivityPeriod.objects.filter(user=user_id)
            serializer = ActivitySerializer(queryset, many=True)
            context['user'] = True
            context['user_id'] = user_id
        context['data'] = serializer.data
        return render(request, 'activitymanager/activity_manager.html', context)

    def delete(self, request, user_id=None, format=None):
        if user_id is None:
            ActivityPeriod.objects.all().delete()
        else:
            ActivityPeriod.objects.filter(user=user_id).delete()
        return Response(status=status.HTTP_200_OK)