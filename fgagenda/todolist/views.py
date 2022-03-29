from django.views.generic import ListView, DetailView, FormView, View
from django.views.generic.edit import CreateView, UpdateView, DeleteView
#from django.core.exceptions import ValidationError
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

#def post_todolist(request):
#    return render(
#        request,
#        'todolist.html',
#        {'todolist':ToDoList.objects.all()}
#    )

def criar_todo_list(request):
    context = {}
    context['form'] = ToDoForms
    context['all_items'] = ToDoList.objects.all()
    return render(request, 'todolist.html', context)

def adicionar_tarefa(request):
    x = request.POST['content']
    # if (x == NULL):
    #    raise ValidationError('Impossível adicionar tarefa vazia.')
    new_item = ToDoList(tarefa = x)
    new_item.save()
    return HttpResponseRedirect('/todolist/')

def editar_tarefa(request, pk):
    coteudo_nova_tarefa = request.POST.get('tarefa', False)
    ToDoList.objects.filter(pk=pk).update(tarefa=coteudo_nova_tarefa)
    return HttpResponseRedirect('/todolist/')
    #coteudo_nova_tarefa = request.POST['content']
    #obj = ToDoList.objects.get(pk=pk)
    #obj.tarefa = coteudo_nova_tarefa
    #obj.save()

class Editar_tarefa(UpdateView):
    template_name='update_product_type.html'
    model = ToDoList

    fields = [
        'tarefa'
    ]
    success_url = reverse_lazy('criar_todo_list')

def deletar_tarefa(request, i):
    y = ToDoList.objects.get(id=i)
    y.delete()
    return HttpResponseRedirect('/todolist/') 