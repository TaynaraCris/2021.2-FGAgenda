from django.db import models
from django.core import validators
from django.utils.translation import ugettext_lazy as _
from django.utils import timezone

from todolist.models import ToDoList


class Meta(models.Model):
    
    class Meta:
        verbose_name = _("Meta")
        verbose_name_plural = _("Metas")

    todolist = models.ForeignKey(
        ToDoList,
        on_delete=models.RESTRICT,
        related_name="todolist",
        verbose_name = _("Lista de Tarefas"),
        editable=True,
        blank=True,
        null=True
    )

    nome = models.CharField(
        verbose_name=_("Nome"),
        unique = True,
        max_length=50,
        blank=False
    )

    descricao = models.TextField(
        verbose_name=_("Descrição"),
        max_length=200,
        blank=True,
        null=True
    )

    dataInicio = models.DateTimeField(
        #verbose_name=_("Data Inicio"),
        default=timezone.now
    )

    dataFim = models.DateTimeField(
        verbose_name=_("Data Fim"),
        blank=True,
        null=False,
    )

    def configura_data_inicio(self):
        self.dataInicio = timezone.now()
        self.save()
