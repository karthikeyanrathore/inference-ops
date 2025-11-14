
from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from mgmt.serialize import OrganizationSerializer 

from django.views import generic

class JSONResponse(HttpResponse):
    def __init__(self, data, **kwargs):
        content = JSONRenderer().render(data)
        kwargs['content_type'] = 'application/json'
        super(JSONResponse, self).__init__(content, **kwargs)


class HealthCheck(generic.ListView):
    http_method_names = ["get"]

    def get(self, request):
        return JSONResponse({"message": "Ok, server health"})

    def http_method_not_allowed(self, *args, **kwargs):
        method = self.request.method
        return JSONResponse({"message": f"HTTP method {method} not allowed"}) 


class CreateOrganization(View):
    @csrf_exempt
    def post(self, request):
        data = JSONParser().parse(request)
        serializer = OrganizationSerializer(data=data)
        if not (serializer.is_valid()):
            return JSONResponse(serializer.errors, status=400)
        
        return JSONResponse({'messsage': 'Ok'}, status=201)
