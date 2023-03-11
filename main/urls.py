from django.contrib import admin
from django.urls import path, include
from .views import ItemListView, CategoriesView, search, ItemListFunc, register, user_login, item_detail
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', ItemListFunc, name='home'),
    path('item/<int:pk>/', item_detail, name='item-detail'),
    path('category/<int:pk>', CategoriesView.as_view(), name='category-detail'),
    path('accounts/register/', register, name='register'),
    path('accounts/login/', user_login, name='login'),
    path('search/<str:search_item>', search, name='search'),
    # path('add-oreder/', add_order, name='add_order'),

]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

