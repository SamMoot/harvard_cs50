from django.urls import path
from . import views

app_name = "tasks"

urlpatterns = [
    path("", views.index, name="index"),
    path("add", views.add, name = "add"), 
    path("add_2", views.add_option2, name = "add_2")
]