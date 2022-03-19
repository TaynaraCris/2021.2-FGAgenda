from django.urls import path
from .views import *

urlpatterns = [
  path('', post_todolist, name="post_todolist"),
]

