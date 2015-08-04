from django.shortcuts import render_to_response
from django.template import RequestContext
import ldap
from .forms import Username_Query_Form
from lookup_form import common

# Create your views here.
            #062979
            #010037754
            #print(results[beg_flag:end_flag])
            #010482287

def index(request):
    context = RequestContext(request)
    if request.method == 'POST':
        form = Username_Query_Form(request.POST)

        if form.is_valid():
            user_birthdate = str(form.cleaned_data['birthdate'])
            user_id = str(form.cleaned_data['id'])
            results = str(search(build_query(user_birthdate, user_id)))

            if results == '[]':
                result = 'No results found based on what you entered. Try again or call the ITS Service Desk at (505) ' \
                         '224-4357.'
                context_dict = {'form': form, 'result': result}

                return render_to_response('lookup_form/index.html', context_dict, context)

            beg_flag = results.find('mail') + 9
            end_flag = results.find('@cnm.edu')
            error = form.errors.as_data()
            result = 'Your username is: ' + results[beg_flag:end_flag]
            context_dict = {'form': form, 'result': result, 'error': error}

            return render_to_response('lookup_form/index.html', context_dict, context)

        else:

            context_dict = {'form': form,}
            return render_to_response('lookup_form/index.html', context_dict, context)
    else:
        form = Username_Query_Form()
        context_dict = {'form': form}

        return render_to_response('lookup_form/index.html', context_dict, context)


def build_query(user_birthdate, user_id):
    birthdate_query = '(extensionAttribute4=' + str(user_birthdate) + ')'
    id_query = '(employeeID=' + str(user_id) + ')'
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