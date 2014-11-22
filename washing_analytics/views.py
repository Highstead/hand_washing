import json

from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return render(request, 'index.html')


def wash(request):

    return_map = {}
    user = request.user
    if user.is_authenticated():
        return_map["success"] = 'success'
        return_map["Method"] = request.method

        # Return status code: 201 - Created
        return HttpResponse(json.dump(return_map), content_type='application/json', status=201)

    # Return status code: 401 - Unauthorized
    return HttpResponse("User unauthenticated", status=401)