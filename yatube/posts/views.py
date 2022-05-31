from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("Index page, nothing here.")

def group_posts(request, slug):
    return HttpResponse("Nothing here yet, but you can still use this link: https://youtu.be/dQw4w9WgXcQ")
