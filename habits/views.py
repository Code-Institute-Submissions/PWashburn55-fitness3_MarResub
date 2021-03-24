from django.shortcuts import render, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.db.models.functions import Lower

from .models import Habit
from .forms import HabitForm


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


@login_required
def add_habit(request):
    """ Add a new habit """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    if request.method == 'POST':
        form = HabitForm(request.POST, request.FILES)
        if form.is_valid():
            habit = form.save()
            messages.success(request, 'Successfully added habit')
            return redirect(reverse('habit_detail', args=[habit.id]))
        else:
            messages.error(request, 'Failed to add habit.'
                           'Please ensure the form is valid.')
    else:
        form = HabitForm()

    template = 'habits/add_habit.html'
    context = {
        'form': form,
    }

    return render(request, template, context)


@login_required
def edit_habit(request, habit_id):
    """ Edit a habit """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    habit = get_object_or_404(Habit, pk=habit_id)
    if request.method == 'POST':
        form = HabitForm(request.POST, request.FILES, instance=habit)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully updated habit!')
            return redirect(reverse('habit_detail', args=[habit.id]))
        else:
            messages.error(request, 'Failed to update habit.'
                           'Please ensure the form is valid.')
    else:
        form = HabitForm(instance=habit)
        messages.info(request, f'You are editing {habit.name}')

    template = 'habits/edit_habit.html'
    context = {
        'form': form,
        'habit': habit,
    }

    return render(request, template, context)


@login_required
def delete_habit(request, habit_id):
    """ Delete a habit from the store """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    habit= get_object_or_404(Habit, pk=habit_id)
    habit.delete()
    messages.success(request, 'Habit deleted!')
    return redirect(reverse('habits'))

