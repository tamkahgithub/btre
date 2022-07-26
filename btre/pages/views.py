from django.shortcuts import render

# Create your views here.
# create a function for the index link to urls API route
def index(request):
    return HttpResponse("<h1>Hello</h1>")