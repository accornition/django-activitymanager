from django.db import models
from django.utils import timezone
import pytz

from django.contrib.auth.signals import user_logged_in, user_logged_out 
from django.dispatch import receiver 
from django.conf import settings


# Create your models here.
class ActivityPeriod(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='active_user', db_column='user', on_delete=models.CASCADE)
    start_time = models.DateTimeField(db_column='start_time', default=timezone.now)
    end_time = models.DateTimeField(db_column='end_time', null=True, blank=True)
