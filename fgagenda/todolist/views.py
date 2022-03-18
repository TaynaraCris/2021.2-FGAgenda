from django.views.generic import ListView, DetailView, FormView, View
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.shortcuts import redirect, render
from django.conf import settings
from .models import *
#from .forms import *
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

# Create your views here.

class ListToDoList(ListView):
    template_name = "todolist.html"
    model = ToDoList

