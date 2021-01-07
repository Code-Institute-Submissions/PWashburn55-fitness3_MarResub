from django.shortcuts import render
from .models import Workout


def all_workouts(request):
    """ A view to show all workouts, including search queries """

    workouts = Workout.objects.all()

    context = {
        'workouts': workouts,
    }

    return render(request, 'workouts/workouts.html', context)



