from django.shortcuts import render
from rest_framework.response import Response 
from rest_framework.decorators import api_view
from rest_framework import status

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import Book
from .serializers import BookSerializer

# Create your views here.
@api_view(['GET','POST'])
def book_list(request):

    if request.method == "GET":
        data = []
        next_page = 1
        previous_page = 1
        books = Book.objects.all()
        page = request.GET.get('page', 1)
        paginator = Paginator(books, 10)
        try: 
            data = paginator.get_page(page)
        except PageNotAnInteger:
            data = paginaor.get_page(1)
        except EmptyPage:
            data = paginator.get_page(paginaotr.num_pages)

        serializer = BookSerializer(data, context = {
            'request':request
        },many=True)

        if data.has_next():
            next_page = data.next_page_number()
        if data.has_previous():
            previous_page = data.previous_page_number()
        
        return Response({
            'data': serializer.data,
            'count': paginator.count,
            'numpages': paginator.num_pages,
            'nextlink' : '/api/books/?page='+str(next_page),
            'prevlink' : 'api/books/?page='+str(previous_page)
        })

    elif request.method == "POST":
        data=[]
        book = Book()
        serializer = BookSerializer(book, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET','PUT','DELETE'])
def books_detail(request, pk):
    try:
        book = Book.objects.get(pk=pk)
    except Book.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer = BookSerializer(book, context={'request':request})
        return Response(serializer.data)

    elif request.method == "PUT":
        serializer = BookSerializer(book, data=request.data, context={'request':request})
        if serialzier.is_valid():
            serialzer.save()
            return Response(serialzer.data)
        return Response(serialzer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        book.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
