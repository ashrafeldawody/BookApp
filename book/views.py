import os
from django.shortcuts import get_object_or_404, render
from django.views.generic.edit import CreateView,DeleteView,UpdateView

from book.models import Book
from book.serializers import BookSerializer




def get_all(request):
    books = Book.objects.all()
    return render(request, 'book/index.html', {"books": books})


def get_by_id(request, book_id):
    book = Book.objects.get(id=book_id)
    book.image = os.path.basename(book.image.name)
    return render(request, 'book/show.html', {"book": book})


class CreateBook(CreateView):
    model = Book
    template_name = "book/create.html"
    fields =  "__all__"

class UpdateBook(UpdateView):
    model = Book
    template_name = "book/create.html"
    fields =  "__all__"

class DeleteBook(DeleteView):
    model = Book
    template_name = "book/delete.html"
    success_url = "/book"