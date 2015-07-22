from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext, loader
from .models import Username_Query
# Create your views here.

def index(request):
    if request.method == 'GET':
        form = Username_Query()
        context = {'form': form}

        return render(request, 'lookup_form/index.html', context)

    elif request.method == 'POST':
        form = Username_Query(request.POST)

        if form.is_valid():
            form.save()

            results = {}
            context = {'form': form, 'results': results,}

            return render(request, 'lookup_form/index.html', context)


