from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.http import Http404, HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, DetailView
from .models import Burner, Category, Heater, AllItems, Images, Order
from django.db.models import Q
from .forms import UserRegistrationForm, LoginForm


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


# class ItemDetailView(DetailView):
#     template_name = 'main/item_detail.html'
#     context_object_name = 'data'
#
#     def get_object(self, queryset=AllItems.objects):
#         pk = self.kwargs.get(self.pk_url_kwarg, None)
#         try:
#             return {'item_detail': Burner.objects.get(item_id=pk), 'images': Images.objects.filter(item_id=pk),
#                     'categories': Category.objects.all()}
#         except:
#             try:
#                 return {'item_detail': Heater.objects.get(item_id=pk), 'images': Images.objects.filter(item_id=pk),
#                         'categories': Category.objects.all()}
#             except:
#                 Http404('No such item')


def item_detail(request, pk):

    if request.method == 'POST':
        quantity = request.POST.get('quantity')
        username = request.user
        user_id = User.objects.get(username=username).id
        Order.objects.create(quantity=quantity, user_id=user_id, item_id=pk)
        return redirect('/')
    else:
        ctx = {}
        try:
            ctx = {'data':
                       {'item_detail': Burner.objects.get(item_id=pk), 'images': Images.objects.filter(item_id=pk),
                        'categories': Category.objects.all()
                        }
                   }
        except:
            try:
                ctx = ctx = {'data':
                       {'item_detail': Heater.objects.get(item_id=pk), 'images': Images.objects.filter(item_id=pk),
                        'categories': Category.objects.all()
                        }
                   }
            except:
                Http404('No such item')

        return render(request, 'main/item_detail.html', ctx)


class CategoriesView(DetailView):
    template_name = 'main/categories.html'
    context_object_name = 'data'

    def get_object(self, queryset=AllItems.objects):
        try:
            pk_url = self.kwargs.get(self.pk_url_kwarg, None)
            # print(queryset.filter(category=pk_url))
            return {'items': queryset.filter(category=pk_url), 'categories': Category.objects.all()}
        except:
            Http404('No such item')


def search(request, search_item):
    items = AllItems.objects.filter(Q(name_lower__icontains=request.GET.get('search').lower()))
    ctx = {
        'data': {
            'items': items,
            'categories': Category.objects.all(),
        }
    }
    return render(request, 'main/searchitems.html', context=ctx)


def register(request):
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            email = user_form.cleaned_data.get('email')
            new_user = User.objects.create(username=email, email=email)
            new_user.set_password(user_form.cleaned_data['password'])
            new_user.save()
            return redirect('/')
    else:
        user_form = UserRegistrationForm()
    return render(request, 'registration/register.html', {'form': user_form})


def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(username=cd['email'], password=cd['password'])

            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect('/')
                else:
                    return HttpResponse('Disabled account')
            else:
                return HttpResponse('Invalid login')
    else:
        form = LoginForm()
    return render(request, 'registration/login.html', {'form': form})

