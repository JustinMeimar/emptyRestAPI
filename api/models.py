from django.db import models
from datetime import datetime
# Create your models here.

class Book(models.Model):
    book_title = models.CharField(max_length=200)
    author_first= models.CharField(max_length=20)
    author_last = models.CharField(max_length=25)
    date_published = models.DateField(default=datetime.now)
    genre = models.CharField(max_length=50)

    def __str__(self):
        return self.book_title