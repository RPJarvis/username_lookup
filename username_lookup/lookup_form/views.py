from django.shortcuts import render_to_response, HttpResponse
from django.template import RequestContext
from .models import Username_Query
import ldap
import json
from .forms import Username_Query_Form
from lookup_form import common
# Create your views here.
            #062979
            #010037754
            #print(results[beg_flag:end_flag])

def index(request):
    context = RequestContext(request)
    if request.method == 'POST':
        form = Username_Query_Form(request.POST)

        if form.is_valid():
            user_birthdate = form.cleaned_data['birthdate']
            user_id = form.cleaned_data['id']
            results = str(search(build_query(user_birthdate, user_id)))
            if results == '':
                results = 'That didnt work'

            beg_flag = results.find('mail') + 9
            print(beg_flag)
            end_flag = results.find('@cnm.edu')
            result = results[beg_flag:end_flag]
            context_dict = {'form': form, 'result': result,}

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


def build_query(user_birthdate, user_id):
    #TODO: why is this chopping a digit?
    birthdate_query = '(extensionAttribute4=' + str(0) + str(user_birthdate) + ')'
    id_query = '(employeeID=' + str(0) + str(user_id) + ')'
    #010482287
    final_query = '(&(objectClass=person)' + id_query + birthdate_query + ')'

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