from django.urls import path

from auther.views import get_all,get_by_id

urlpatterns = [
    path('', get_all),
    path('<int:auther_id>/', get_by_id,name="auther_view"),
]
