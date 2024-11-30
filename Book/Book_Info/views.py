from django.shortcuts import render
from .models import Author, Book, Review



def author_list(request):
    authors = Author.objects.all
    return render(request, 'authors.html', {'authors': authors})

def home(request):
    books = Book.objects.all
    return render(request, 'index.html', {'books': books})

def reviews_list(request):
    reviews = Review.objects.all
    return render(request, 'reviews.html', {'reviews': reviews})