from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Burner, Category


class ItemListView(ListView):
    queryset = Burner.objects.order_by('-upload_at')
    context_object_name = 'data'
    template_name = 'main/index.html'

    def get_queryset(self):
        queryset = {
            'burners': Burner.objects.all(),
            'categories': Category.objects.all()
        }
        return queryset


class ItemDetailView(DetailView):
    model = Burner
    template_name = 'main/item_detail.html'
