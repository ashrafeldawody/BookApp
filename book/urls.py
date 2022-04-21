from django.urls import path

from book.views import CreateBook,DeleteBook,UpdateBook, get_all,get_by_id

urlpatterns = [
    path('', get_all,name="book_index"),
    path('create/', CreateBook.as_view(),name="book_create"),
    path('<int:pk>/delete', DeleteBook.as_view(),name="book_delete"),
    path('<int:pk>/edit', UpdateBook.as_view(),name="book_edit"),
    path('<int:book_id>/', get_by_id,name="book_view"),
]
