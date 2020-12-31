from django.shortcuts import render, get_object_or_404
from .models import Habit

# Create your views here.


def all_habits(request):
    """ A view to show all habits, including search queries """

    habits = Habit.objects.all()

    context = {
        'habits': habits,
    }

    return render(request, 'habits/habits.html', context)


def habit_detail(request, habit_id):
    """ A view to show habit detail page """

    habit = get_object_or_404(Habit, pk=habit_id)

    context = {
        'habit': habit,
    }

    return render(request, 'habits/habit_detail.html', context)
