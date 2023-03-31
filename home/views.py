from django.shortcuts import redirect, render, HttpResponse
from django.contrib import messages
from .models import Book, Contact
from django.utils import timezone
from .models import Book, BookIssue
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib.auth import logout, login
from django.contrib.auth.decorators import login_required
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

def lists(request):
   issue = BookIssue.objects.filter(student=request.user)
   return render(request, 'lists.html', {'issue': issue})
    # return HttpResponse("this is aboutpage")

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

def logout_view(request):
    logout(request)
    return redirect('/login')

def contact(request):
    # return HttpResponse("this is contactpage")
    if request.method =="POST":
        name=request.POST.get("name")
        contact=request.POST.get("contact")
        email=request.POST.get("email")
        address=request.POST.get("address")
        grivance=request.POST.get("grivance")
        contact=Contact(name=name, contact=contact, email=email, address=address, grivance=grivance)
        contact.save()
        messages.success(request, 'Form has been sent successfully!.')
       
    return render(request, 'contact.html')


@login_required
def issue_book(request, book_id):
    book = Book.objects.get(id=book_id)

        # check if book is available for issue
    if book.copies <= 0:
        return render(request, 'error.html', {'error_message': 'This book is not available for issue'})

        # create a new book issue object
    issue = BookIssue(book=book, student=request.user, due_date=timezone.now() + timezone.timedelta(days=14))
    issue.save()
    messages.success(request, 'Books has been sent successfully!.')
    

        # update the book copy count
    book.copies -= 1
    book.save()

    return redirect('book_list')

    # Handle GET requests
    book = Book.objects.get(id=book_id)
    return render(request, 'books.html', {'book': book})


@login_required
def return_book(request, issue_id):
    issue = BookIssue.objects.get(id=issue_id)

    # check if book has already been returned
    if issue.returned:
        return render(request, 'error.html', {'error_message': 'This book has already been returned'})

    # update the book issue object to indicate it has been returned
    issue.returned = True
    issue.save()

    # update the book copy count
    book = issue.book
    book.copies += 1
    book.save()

    return redirect('book_list')

@login_required
def all_books(request):
    books = Book.objects.all()
    issue = BookIssue.objects.filter(student=request.user)
    # return render(request, 'lists.html', {'issue': issue})
    context = {'books': books, 'issue': issue}
    return render(request, 'books.html', context)
    
def book_list(request):
    issues =Contact.objects.all()
    return render(request, 'books.html', {'issues': issues})
    






