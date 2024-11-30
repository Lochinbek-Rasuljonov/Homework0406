from django.db import models
from django.db.models import ForeignKey
from django.core.exceptions import ValidationError


class Author(models.Model):
    first_name = models.CharField(max_length= 100)
    last_name = models.CharField(max_length= 100)
    date_of_birth = models.DateField(blank= True, null= True)
    date_of_death = models.DateField(blank=True, null=True)
    biography = models.TextField(blank= True, null= True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"



class Book(models.Model):
    title = models.CharField(max_length= 200)
    author = models.ForeignKey(Author, on_delete= models.CASCADE)
    publication_date = models.DateField()
    isbn = models.CharField(max_length= 13, unique= True)
    genre = models.CharField(max_length= 100)
    summary = models.TextField(blank= True, null= True)
    book_photo = models.ImageField(upload_to= 'photo/')

    def __str__(self):
        return self.title



class Review(models.Model):
    book = models.ForeignKey(Book, related_name='reviews', on_delete= models.CASCADE)
    reviewer_name = models.CharField(max_length= 100)
    rating = models.PositiveSmallIntegerField()
    comment = models.TextField(blank= True, null= True)
    created_at = models.DateTimeField(auto_now_add= True)

    def clean(self):
        if not (1 <= self.rating <= 5):
            raise ValidationError("Baho 1 va 5 oralig'ida bo'lishi kerak.")

    def __str__(self):
        return f"{self.book} | {self.reviewer_name}"
