from django.shortcuts import render
from django.views.generic import ListView
from .models import Burner


class IndexView(ListView):
    queryset = Burner.objects.all()
    context_object_name = 'data'
    template_name = 'main/index.html'
