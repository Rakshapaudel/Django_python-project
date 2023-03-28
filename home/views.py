from django.shortcuts import redirect, render, HttpResponse
from django.contrib import messages
from home.models import Contact
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib.auth import logout, login
# from datetime import datetime
# Create your views here.
def index(request):
    if request.user.is_anonymous:
        return redirect('/login')
    context = {
        'vaariable':"this is sent"
    }
    
    #return HttpResponse("this is homepage")
    return render(request, 'index.html')

def about(request):
   return render(request, 'about.html')
    # return HttpResponse("this is aboutpage")

def services(request):
   return render(request, 'services.html')
    # return HttpResponse("this is servicespage")

def loginuser(request):
    if request.method=="POST":
        username=request.POST.get('name')
        password = request.POST.get('password')
     
     
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            return render(request, 'login.html')

     

    return render(request, 'login.html')

def contact(request):
    # return HttpResponse("this is contactpage")
    if request.method =="POST":
        name=request.POST.get("name")
        contact=request.POST.get("contact")
        email=request.POST.get("email")
        address=request.POST.get("address")
        contact=Contact(name=name, contact=contact, email=email, address=address)
        contact.save()
        messages.success(request, 'Form has been sent successfully!.')
       
    return render(request, 'contact.html')