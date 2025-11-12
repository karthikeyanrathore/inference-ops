
from django.shortcuts import render
from django.http import JsonResponse

from django.views import generic

class HealthCheck(generic.ListView):
    http_method_names = ["get"]

    def get(self, request):
        return JsonResponse({"message": "Ok, server health"})

    def http_method_not_allowed(self, *args, **kwargs):
        method = self.request.method
        return JsonResponse({"message": f"HTTP method {method} not allowed"}) 


