#from msilib.schema import Class
#from tkinter import Widget
from django import forms
from .models import ToDoList
#from django.core.exceptions import ValidationError


class ToDoForms(forms.ModelForm):
    
#    def min_validation(value):
#        if len(value) < 1:
#            raise ValidationError("{} não é valido, o campo não deve ser vazio.". format(value))
    
#    def __init__(self, *args, **kwargs):
#        super(ToDoList, self).__init__(*args, **kwargs)
#        self.fields["tarefa"].validators.append(min_validation)    
 
    class Meta:
        model = ToDoList
        fields = [
            "tarefa"
        ]
        widgets = {
            "tarefa": forms.TextInput()
        }
    
    