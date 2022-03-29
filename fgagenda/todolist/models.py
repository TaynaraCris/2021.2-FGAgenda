from django.db import models
from django.core import validators
from django.utils.translation import ugettext_lazy as _


class ToDoList(models.Model):
    """
    Abstract class that represents class 'Component' in Composite Pattern.
    """
    
    class Meta:
        verbose_name = _("Lista de Tarefa")
        verbose_name_plural = _("Lista de Tarefas")
    
    tarefa = models.CharField(
        verbose_name=_("Tarefa"),
        max_length=50,
        editable=True,
        blank=False,
        null=True
    )
