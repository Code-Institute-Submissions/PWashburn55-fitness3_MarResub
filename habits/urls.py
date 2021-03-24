from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_habits, name='habits'),
    path('<int:habit_id>/', views.habit_detail, name='habit_detail'),
    path('add/', views.add_habit, name='add_habit'),
    path('edit/<int:habit_id>/', views.edit_habit, name='edit_habit'),
    path('delete/<int:habit_id>/', views.delete_habit, name='delete_habit'),
]
