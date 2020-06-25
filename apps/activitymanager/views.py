from django.shortcuts import render
from rest_framework import generics, permissions
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import BasicAuthentication, SessionAuthentication
from rest_framework.views import APIView

from apps.accounts.models import User

# Create your views here.
def index(request):
    return render(request, 'activitymanager/index.html', {})

def room(request):
    if request.user.is_authenticated and request.user.is_superuser:
        admin = True
    else:
        admin = False

    context = { 'admin': admin }
    return render(request, 'activitymanager/activity_manager.html', context)