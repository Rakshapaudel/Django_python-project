from django.contrib import admin
from .models import Contact, Book, BookIssue

# Register your models here.
admin.site.register(Contact)
admin.site.register(Book)
admin.site.register(BookIssue)


