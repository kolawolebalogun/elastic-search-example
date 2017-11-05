from django.shortcuts import render_to_response
from django.http import JsonResponse
from elasticsearchapp.util import util
from django.http import HttpResponse


# Create your views here.

def search(request):
    return render_to_response('search.html', {'result': {}})


# Search api
def api_search(request):
    if request.method == "GET":
        q = request.GET.get('q')
        if q:
            result = util.search(q)
            return JsonResponse(result, json_dumps_params={'indent': 2})

    return HttpResponse(status=403)