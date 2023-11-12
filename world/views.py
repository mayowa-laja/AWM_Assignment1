from django.core.serializers import serialize
from django.http import JsonResponse
from django.shortcuts import render
from world.models import WorldBorder

# Create your views here.


def pop_query(request):
    if request.method == 'GET':
        queryset_data = WorldBorder.objects.filter(pop2005__lt=1000000)

        context = {'queryset_data': queryset_data}

        return render(request, 'population.html', context)


def pop_query_json(request):
    if request.method == 'GET':
        queryset_data = WorldBorder.objects.filter(pop2005__lt=1000000)

        data = serialize('json', queryset_data)

        return JsonResponse(data, safe=False)

