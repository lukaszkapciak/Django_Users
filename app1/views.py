from django.shortcuts import render
from .models import Book
from django.views.generic import ListView, DetailView

# Create your views here.

def Home(request):
    title = 'My books'
    books = Book.objects.all()
    return render(request, 'home.html', {'title': title, 'books': books})