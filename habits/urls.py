from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_habits, name='habits'),
    path('<habit_id>', views.habit_detail, name='habit_detail'),
]
