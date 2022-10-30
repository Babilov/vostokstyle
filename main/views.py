from django.http import Http404
from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView
from .models import Burner, Category, AllItems # TestBurner, TestBurner


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
    context_object_name = 'data'

    def get_object(self, queryset=Burner.objects):
        pk = self.kwargs.get(self.pk_url_kwarg, None)
        try:
            return {'item_detail': queryset.get(pk=pk), 'categories': Category.objects.all()}
        except:
            raise Http404('No such object')


# class ItemSearchListView(ListView):
#     # queryset =
#     context_object_name = 'data'
#     template_name = 'main/searchItems.html'


# def show_category_items(request, category_slug_items):
#     category_id = Category.objects.get(slug=category_slug_items).id
#     try:
#         items = Burner.objects.get(category=category_id)
#     except:
#         items =


class TestView(ListView):
    queryset = AllItems.objects.all()
    context_object_name = 'data'
    print(queryset)
    template_name = 'main/test.html'

