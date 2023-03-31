from django.contrib import admin
from django.urls import path
from home import views

urlpatterns = [
   path("", views.index, name='home'),
   path("about", views.about, name='about'),
   path("lists", views.lists, name='lists'),
   path("services", views.services, name='services'),
   path("contact", views.contact, name='contact'),
   path("login", views.loginuser, name='contact'),
   path("book_list/", views.book_list, name='book_list'),
   path('books/', views.all_books, name='all_books'),
   path('issue_book/<int:book_id>/', views.issue_book, name='issue_book'),
   path("return_book", views.return_book, name='return_book'),
   
   # path('my_books/', views.my_books, name='my_books'),
   path('logout_view/', views.logout_view, name='logout_view'),
   
]
