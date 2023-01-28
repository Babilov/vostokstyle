from django.http import Http404
from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView
from .models import Burner, Category, Heater, AllItems, Images
from django.db.models import Q
from .forms import SearchForm


def ItemListFunc(request):
    ctx = {
       'data': {
           'burners': Burner.objects.all(),
           'heaters': Heater.objects.all(),
           'categories': Category.objects.all(),
       }
    }
    return render(request, 'main/index.html', context=ctx)


class ItemListView(ListView):
    context_object_name = 'data'
    template_name = 'main/index.html'

    # def get_queryset(self):
    #     queryset = {
    #         'burners': Burner.objects.all(),
    #         'heaters': Heater.objects.all(),
    #         'categories': Category.objects.all(),
    #     }
    #     return queryset
    #
    # def get(self, request, *args, **kwargs):
    #     return super(ItemListView, self).get(request, *args, **kwargs)


class ItemDetailView(DetailView):
    template_name = 'main/item_detail.html'
    context_object_name = 'data'

    def get_object(self, queryset=AllItems.objects):
        pk = self.kwargs.get(self.pk_url_kwarg, None)
        try:
            return {'item_detail': Burner.objects.get(item_id=pk), 'images': Images.objects.filter(item_id=pk),
                    'categories': Category.objects.all()}
        except:
           try:
               return {'item_detail': Heater.objects.get(item_id=pk), 'images': Images.objects.filter(item_id=pk),
                    'categories': Category.objects.all()}
           except:
               Http404('No such item')


class CategoriesView(DetailView):
    template_name = 'main/categories.html'
    context_object_name = 'data'

    def get_object(self, queryset=AllItems.objects):
        try:
            pk_url = self.kwargs.get(self.pk_url_kwarg, None)
            print(queryset.filter(category=pk_url))
            return {'items': queryset.filter(category=pk_url), 'categories': Category.objects.all()}
        except:
            Http404('No such item')


def search(request, search_item):
    items = AllItems.objects.filter(Q(name__icontains=request.GET.get('search')))
    ctx = {
        'data': {
            'items': items,
            'categories': Category.objects.all()
        }
    }
    return render(request, 'main/searchitems.html', context=ctx)
