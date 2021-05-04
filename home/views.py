from django.shortcuts import render, HttpResponse
from datetime import datetime
from home.models import Contact
from django.contrib import messages
# Create your views here.

def index(request):
    return render(request, 'index.html')

def gallery(request):
    return render(request, 'gallery.html')


def contact(request):
    if request.method=="POST":
        name=request.POST.get('name')
        email=request.POST.get('email')
        phone=request.POST.get('phone')
        desc=request.POST.get('desc')

        contact=Contact(name=name, email=email, phone=phone, desc=desc, date=datetime.today())
        contact.save()
        messages.success(request, 'Your form has been submitted.')

    return render(request, 'contact.html')


def about(request):
    return render(request, 'about.html')

def trainer(request):
    return render(request, 'trainer.html')

def membership(request):
    return render(request, 'membership.html')

def terms(request):
    return render(request, 'terms.html')

def location(request):
    return render(request, 'location.html')

