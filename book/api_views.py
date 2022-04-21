from django.shortcuts import render
from django.http.response import JsonResponse
from book.models import Book
from book.serializers import BookSerializer
from rest_framework.parsers import JSONParser 
from rest_framework import status
 
from rest_framework.decorators import api_view

def get_all(request):
    try: 
        book = Book.objects.all() 
    except Book.DoesNotExist: 
        return JsonResponse({'message': 'The Book does not exist'}) 
    book_serializer = BookSerializer(book, many=True) 
    return JsonResponse(book_serializer.data, safe=False)

@api_view(['GET'])
def get_by_id(request,pk):
    try: 
        book = Book.objects.get(pk=pk)
    except Book.DoesNotExist: 
        return JsonResponse({'message': 'The Book does not exist'}) 
    book_serializer = BookSerializer(book) 
    return JsonResponse(book_serializer.data) 

@api_view(['POST'])
def create(request):
    book_data = JSONParser().parse(request)
    book_serializer = BookSerializer(data=book_data)
    if book_serializer.is_valid():
        book_serializer.save()
        return JsonResponse(book_serializer.data) 
    return JsonResponse(book_serializer.errors)
@api_view(['PUT'])
def update(request,pk):
    try: 
        book = Book.objects.get(pk=pk) 
    except Book.DoesNotExist: 
        return JsonResponse({'message': 'The Book does not exist'}) 

    book_data = JSONParser().parse(request) 
    book_serializer = BookSerializer(book, data=book_data) 
    if book_serializer.is_valid(): 
        book_serializer.save() 
        return JsonResponse(book_serializer.data) 
    return JsonResponse(book_serializer.errors) 

@api_view(['DELETE'])
def delete(request,pk):
    try: 
        book = Book.objects.get(pk=pk) 
    except Book.DoesNotExist: 
        return JsonResponse({'message': 'The Book does not exist'}) 

    book.delete() 
    return JsonResponse({'message': 'The Book was deleted successfully!'})
