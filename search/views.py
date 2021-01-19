from django.shortcuts import render
from django.db.models import Q
from products.models import Product
from habits.models import Habit
from plans.models import Plan
from itertools import chain


def all_search(request):
    """ A view to show the search query """
    query = ""
    if request.GET:
        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request, "No search criteria entered")
                return redirect(reverse('search'))

            queries = Q(name__icontains=query) | \
                Q(description__icontains=query)
    products = Product.objects.filter(Q(name__contains=query) | Q(description__contains=query))
    habits = Habit.objects.filter(Q(name__contains=query) | Q(description__contains=query))
    plans = Plan.objects.filter(Q(name__contains=query) | Q(description__contains=query))
    results = chain(products, habits, plans)
    query = None
    sort = None
    direction = None

    if request.GET:
        if 'sort' in request.GET:
            sortkey = request.GET['sort']
            sort = sortkey
            if sortkey == 'name':
                sortkey = 'lower_name'
                results = results.annotate(lower_name=Lower('name'))
            if 'direction' in request.GET:
                direction = request.GET['direction']
                if direction == 'desc':
                    sortkey = f'-{sortkey}'
            results = results.order_by(sortkey)

        """if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request, "No search criteria entered")
                return redirect(reverse('search'))

            queries = Q(name__icontains=query) | \
                Q(description__icontains=query)
            results = results.filter(queries) """

    current_sorting = f'{sort}_{direction}'

    context = {
        'results': results,
        'search_term': query,
        'current_sorting': current_sorting,
    }

    return render(request, 'search/search_results.html', context)

