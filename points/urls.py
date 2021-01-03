from django.urls import path
from . import views


urlpatterns = [
    path('', views.profile_points, name='profile_points')
]