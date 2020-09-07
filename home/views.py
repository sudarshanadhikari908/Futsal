from django.shortcuts import render,HttpResponse

# Create your views here.
def home(index):
    return HttpResponse("I am from home")
