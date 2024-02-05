from django.shortcuts import render
from django.views.generic import ListView
from .models import ToDoList

class ListListView(ListView):
    model = ToDoList
    template_name = "todo_app/index.html"
# Create your views here.
