from django.urls import path
from .views import *
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('invoice_print/', views.invoice_print, name='invoice_print'),
]