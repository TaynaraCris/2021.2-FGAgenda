from msilib.schema import Class
from django import forms
from .models import ToDoList

class ToDoForms(forms.ModelForm):
    class Meta:
        model = ToDoList
        fields = "__all__"