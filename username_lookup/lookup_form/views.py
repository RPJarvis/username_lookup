from django.shortcuts import render_to_response
from django.template import RequestContext
from .models import Username_Query
import ldap
from lookup_form import common
# Create your views here.

def index(request):
    context = RequestContext(request)
    if request.method == 'GET':
        form = Username_Query()
        context_dict = {'form': form}

        return render_to_response('lookup_form/index.html', context_dict, context)

    elif request.method == 'POST':
        form = Username_Query(request.POST)

        if form.is_valid():
            form.save()
            build_query()
            results = search(build_query())
            context_dict = {'form': form, 'results': results,}

            return render_to_response('lookup_form/index.html', context_dict, context)

        #TODO:else

def build_query():
    query = {}
    return query


def search(query):
    l = ldap.initialize(common.ldap_url)
    l.simple_bind_s(common.ad_user, common.ad_p)
    scope = ldap.SCOPE_SUBTREE
    attributes = common.attributes
    base = common.base
    ldap_filter = query

    results = l.search_s(base, scope, ldap_filter, attributes)
    l.unbind()

    return results