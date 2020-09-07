from django.shortcuts import render,HttpResponse
from django.contrib import messages

# Create your views here.
def home(request):
    return render(request, "home/home.html")



def contact(request):
    messages.success(request, 'Welcome To Contact')
    
        

    return render(request, 'home/contact.html')