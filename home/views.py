from django.contrib import messages
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, DetailView
from django.utils import timezone
from .models import (
    Contact,
    Product,
    Order,
    OrderItem
)


# Create your views here.
def home(request):
    allProds = []
    catprods = Product.objects.values('category', 'id')
    cats = {item['category'] for item in catprods}
    for cat in cats:
        prod = Product.objects.filter(category=cat)
        n = len(prod)
        nSlides = n // 4 + ceil((n / 4) - (n // 4))
        allProds.append([prod, range(1, nSlides), nSlides])
    params = {'allProds': allProds}
    return render(request, 'home/home.html', params)


def contact(request):
    messages.success(request, 'Welcome To Contact')
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        content = request.POST['content']
        if len(name) < 3 or len(email) < 6 or len(phone) < 10 or len(content) < 10:
            messages.error(request, "Please fill the form correctly")
        else:
            contact = Contact(name=name, email=email,
                              phone=phone, content=content)
            contact.save()
            messages.success(request, "Please fill the form correctly")

    return render(request, 'home/contact.html')


def about(request):

    return render(request, 'home/about.html')


def login(request):
    return render(request, 'home/login.html')
