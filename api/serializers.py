from rest_framework import serializers
from .models import Book

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        field = ('pk','book_title','author_first','author_last','date_published','genre')
        fields = '__all__'