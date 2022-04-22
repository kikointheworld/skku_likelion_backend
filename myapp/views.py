from django.shortcuts import render

# Create your views here.


from django.http import HTTPResponse
from django.shortcuts import render

def index(request):
    return HTTPResponse("Hello, Django!")