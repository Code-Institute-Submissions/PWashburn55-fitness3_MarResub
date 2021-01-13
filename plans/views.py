from django.shortcuts import render, get_object_or_404
from .models import Plan
from django.db.models import Q
from django.db.models.functions import Lower


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
