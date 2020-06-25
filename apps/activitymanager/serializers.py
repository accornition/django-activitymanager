from rest_framework import serializers
from django.contrib.auth import authenticate

from apps.accounts.models import User

from .models import ActivityPeriod


class ActivitySerializer(serializers.ModelSerializer):
    class Meta:
        model = ActivityPeriod
        fields = ('user', 'start_time', 'end_time',)