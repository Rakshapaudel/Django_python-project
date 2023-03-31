from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Contact(models.Model):
    name=models.CharField(max_length=122)
    contact=models.CharField(max_length=122)
    email=models.CharField(max_length=122)
    address=models.CharField(max_length=122)
    grivance=models.TextField(null=True)
    
    def __str__(self):
        return self.name

class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    isbn = models.CharField(max_length=13)
    copies = models.PositiveIntegerField()
    def __str__(self):
        return self.title

class BookIssue(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    student = models.ForeignKey(User, on_delete=models.CASCADE)
    issue_date = models.DateField(auto_now_add=True)
    due_date = models.DateField()
    returned = models.BooleanField(default=False)
    def __str__(self):
        return f"{self.book} issued by {self.student} on {self.issue_date}"