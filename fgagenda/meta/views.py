from urllib.request import Request
from django.views.generic import ListView, DetailView, FormView, View
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.shortcuts import redirect, render
from django.conf import settings
from .models import *
from .forms import *

class CriarMeta(CreateView):
    template_name = 'criar_meta.html'
    model = Meta
    form_class = CriaMetaForm
    success_url = reverse_lazy('home')
    
#def home_view(request):
#    context = {}
#    context['form'] = ToDoForms
#    return render(request, 'todolist.html', context)