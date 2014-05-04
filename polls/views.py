from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def tmp(request):
    #return HttpResponse("Hello, world. You're at the book index.")
    return render(request, 'polls/tmp.html')
