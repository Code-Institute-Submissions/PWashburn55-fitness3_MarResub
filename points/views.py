from django.shortcuts import render


def profile_points(request):
    """ Display the user's points """

    template = 'points/profile_points.html'
    context = {}

    return render(request, template, context)

