from django.views.generic import ListView, DetailView, FormView, View
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.shortcuts import redirect, render
from django.conf import settings
from .models import *
from .forms import *
#from django.contrib.auth.decorators import login_required
#from django.utils.decorators import method_decorator

# Create your views here.

#class ToDoListView(ListView):
    # template_name = "todolist.html"
    #model = ToDoList

    #def get(self, request):
        #return render(request, 'todolist.html.html', {})

    #success_url = reverse_lazy('todolist')

def post_todolist(request):
    return render(
        request,
        'todolist.html',
        {'todolist':ToDoList.objects.all()}
    )

#def home_view(request):
#    context = {}
#    context['form'] = ToDoForms
#    return render(request, 'todolist.html', context)

# "key": "value"
