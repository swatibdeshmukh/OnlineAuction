from msilib.schema import ListView
from urllib import request
from django import views
import django
from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import *
from .forms import *
from django.urls import reverse_lazy

# Create your views here.
class CauntryList(ListView):
    model = Country

class AddCountry(CreateView):
    model = Country
    succes_url = reverse_lazy('')
