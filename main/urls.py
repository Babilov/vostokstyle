from django.contrib import admin
from django.urls import path, include
from .views import ItemListView, ItemDetailView, CategoriesView, search, ItemListFunc
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', ItemListFunc, name='home'),
    path('item/<int:pk>/', ItemDetailView.as_view(), name='item-detail'),
    path('category/<int:pk>', CategoriesView.as_view(), name='category-detail'),
    path('search/<str:search_item>', search, name='search'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

