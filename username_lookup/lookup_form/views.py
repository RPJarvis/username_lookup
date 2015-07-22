from django.shortcuts import render_to_response, HttpResponse
from django.template import RequestContext
from .models import Username_Query
import ldap
import json
from .forms import Username_Query_Form
from lookup_form import common
# Create your views here.

def index(request):
    context = RequestContext(request)
    if request.method == 'POST':
        form = Username_Query_Form(request.POST)

        if form.is_valid():
            #TODO:probably have to uncomment htis below or something i dunno
            #form.save()
            user_birthdate = form.cleaned_data['birthdate']
            user_id = form.cleaned_data['id']
            response_data = {}
            results = search(build_query(user_birthdate, user_id))
            #response_data['results'] = results
            if results == '':
                results = 'That didnt work'

            context_dict = {'form': form, 'results': results,}

            #it might be better to have search as its own url call but leave the data decoupld
            #in order to pass it in to the search function
            return render_to_response('lookup_form/index.html', context_dict, context)
        else:
            #TODO:make this less dumb
            return HttpResponse(
                json.dumps({"Something broke": "fix it"}),
                content_type="application/json"
            )
    else:
        form = Username_Query_Form()
        context_dict = {'form': form}

        return render_to_response('lookup_form/index.html', context_dict, context)

        #TODO:else


def build_query(user_birthdate, user_id):
    birthdate_query = '(extensionattribute4=' + str(user_birthdate) + ')'
    id_query = '(cn=' + str(user_id) + ')'
    final_query = '(&(objectClass=person)' + birthdate_query + id_query + ')'

    return final_query


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