from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext, loader
# Create your views here.

def index(request):
    if request.method == 'GET':
        template = loader.get_template('lookup_form/index.html')
        context = RequestContext(request, {})

        return HttpResponse(template.render(context))

    elif request.method == 'POST':
        template = loader.get_template('lookup_form/index.html')
        context = RequestContext(request, {})

        return HttpResponse(template.render(context))


