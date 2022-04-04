from urllib.request import Request
from django.views.generic import ListView, DetailView, FormView, View
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.shortcuts import redirect, render
from django.conf import settings
from .models import *
from .forms import *
from todolist.forms import *

class MetaView(CreateView):
    template_name = 'criar_meta.html'
    model = Meta
    form_class = MetaForm

    def get_context_data(self):
        context = {}
        #context['todoform'] = ToDoForms
        context['form'] = MetaForm
        context['all_items'] = ToDoList.objects.all()
        return context

    def get_objects(self):
        pass

    success_url = reverse_lazy('inicio')
    
#def home_view(request):
#    context = {}
#    context['form'] = ToDoForms
#    return render(request, 'todolist.html', context)