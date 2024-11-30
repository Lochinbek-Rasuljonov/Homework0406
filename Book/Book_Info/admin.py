from django.contrib import admin

from .models import Author, Book, Review



#AUTHOR
admin.site.register(Author)

#BOOK
admin.site.register(Book)

#REVIEW
admin.site.register(Review)