from django.shortcuts import render
from django.http import JsonResponse

# Create your views here.

def post_list(request):
    data = { 'foo': 'bar' }
    return JsonResponse(data)