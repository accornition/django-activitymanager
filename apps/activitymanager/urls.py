from django.urls import path, include
from . import api
from . import views

urlpatterns = [
    path('activitylist/<int:user_id>', api.ActivityList.as_view()),
	path('activitylist', api.ActivityList.as_view()),    
    path('index', views.index),
    path('room', views.room),
]