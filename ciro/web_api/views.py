from django.shortcuts import render
from .models import Posts, Categories
from django.http import JsonResponse
import json

# Create your views here.
def webapi(request):
    data = list(Posts.objects.values())
    return JsonResponse(data, safe=False)

def web_category(request):
    data = list(Categories.objects.values())
    return JsonResponse(data, safe=False)