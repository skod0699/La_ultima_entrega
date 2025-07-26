from django.urls import path
from . import views  # Importa las vistas definidas en views.py
from .views import saludo_con_template, crear_familiar  # Importa la vista específica

urlpatterns = [
  path('hola-mundo-templates/', saludo_con_template),
 path('crear-familiar/<str:nombre>/', views.crear_familiar, name='crear_familiar'),

  



]
