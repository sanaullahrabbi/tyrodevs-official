from django.urls import path
from app_main.views import *

app_name = "app_book"

urlpatterns = [
    path("", index_view, name="home"),
]
