from django.shortcuts import render, get_object_or_404
from .models import Habit

# Create your views here.

def all_habits(request):
    """ A view to show all habits, including search queries """

    habits = Habit.objects.all()

    context = {
        'habits': habits,
    }

    return render(request, 'habit/habits.html', context)
