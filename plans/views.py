from django.shortcuts import render, get_object_or_404
from .models import Plan
from django.db.models import Q
from django.db.models.functions import Lower

from django.contrib import messages
from django.contrib.auth.decorators import login_required


from .models import Plan
from .forms import PlanForm


def all_plans(request):
    """ A view to show all plans, including sorting and search queries """

    plans = Plan.objects.all()
    query = None
    sort = None
    direction = None

    if request.GET:
        if 'sort' in request.GET:
            sortkey = request.GET['sort']
            sort = sortkey
            if sortkey == 'name':
                sortkey = 'lower_name'
                plans = plans.annotate(lower_name=Lower('name'))
            if 'direction' in request.GET:
                direction = request.GET['direction']
                if direction == 'desc':
                    sortkey = f'-{sortkey}'
            plans = plans.order_by(sortkey)

        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request, "No search criteria entered")
                return redirect(reverse('plans'))

            queries = Q(name__icontains=query) | \
                Q(description__icontains=query)
            plans = plans.filter(queries)

    current_sorting = f'{sort}_{direction}'

    context = {
        'plans': plans,
        'search_term': query,
        'current_sorting': current_sorting,
    }

    return render(request, 'plans/plans.html', context)


def plan_detail(request, plan_id):
    """ A view to show individual plan details """

    plan = get_object_or_404(Plan, pk=plan_id)

    context = {
        'plan': plan,
    }

    return render(request, 'plans/plan_detail.html', context)

"""
def all_plans(request):
     A view to show all plans, including search queries 

    plans = Plan.objects.all()

    context = {
        'plans': plans,
    }

    return render(request, 'plans/plans.html', context)
"""


@login_required
def add_plan(request):
    """ Add a new workout """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    if request.method == 'POST':
        form = PlanForm(request.POST, request.FILES)
        if form.is_valid():
            plan = form.save()
            messages.success(request, 'Successfully added plan')
            return redirect(reverse('plan_detail', args=[plan.id]))
        else:
            messages.error(request, 'Failed to add habit.'
                           'Please ensure the form is valid.')
    else:
        form = PlanForm()

    template = 'plans/add_plan.html'
    context = {
        'form': form,
    }

    return render(request, template, context)


@login_required
def edit_plan(request, plan_id):
    """ Edit a plan """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    habit = get_object_or_404(Plan, pk=plan_id)
    if request.method == 'POST':
        form = PlanForm(request.POST, request.FILES, instance=plan)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully updated workout!')
            return redirect(reverse('plan_detail', args=[plan.id]))
        else:
            messages.error(request, 'Failed to update habit.'
                           'Please ensure the form is valid.')
    else:
        form = PlanForm(instance=habit)
        messages.info(request, f'You are editing {plan.name}')

    template = 'plans/edit_plan.html'
    context = {
        'form': form,
        'plan': plan,
    }

    return render(request, template, context)


@login_required
def delete_plan(request, habit_id):
    """ Delete a habit from the store """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    plan= get_object_or_404(Plan, pk=plan_id)
    habit.delete()
    messages.success(request, 'Habit deleted!')
    return redirect(reverse('habits'))


