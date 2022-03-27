from django.urls import path
from .views import *

urlpatterns = [
  path('', criar_todo_list, name="criar_todo_list"),
  path('adicionaTarefa/', adicionar_tarefa, name="adicionar_tarefa"),
  path('deletaTarefa/<int:i>/', deletar_tarefa, name="deletar_tarefa"), 
]

