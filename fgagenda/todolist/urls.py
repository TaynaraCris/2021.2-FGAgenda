from django.urls import path
from django.views.generic import TemplateView

from . views import *

urlpatterns = [
  path('todolist/', ListToDoList.as_view(template_name="todolist.html"), name="todolist"),
]

