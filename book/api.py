from django.urls import include, path

import book.api_views as views

urlpatterns = [ 
    path('', views.get_all,name="api_book_index"),
    path('create', views.create,name="api_book_create"),
    path('<int:pk>/delete', views.delete,name="api_book_delete"),
    path('<int:pk>/edit', views.update,name="api_book_edit"),
    path('<int:pk>', views.get_by_id,name="api_book_view"),
]