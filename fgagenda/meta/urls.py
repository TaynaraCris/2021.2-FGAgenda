#path('create/', CreateProduct.as_view(template_name='create_product.html'), name='create_product')
from django.urls import path
from django.views.generic import TemplateView
from .views import *

urlpatterns = [
  path('', CriaMeta.as_view(template_name='criar_meta.html'), name="criar_meta"),
  path('edita/<int:pk>', EditaMeta.as_view(template_name='editar_meta.html'), name='editar_meta')
]