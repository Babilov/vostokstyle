from django.contrib import admin
from django.urls import path, include
from .views import ItemListView, ItemDetailView, show_category_items
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', ItemListView.as_view(), name='home'),
    path('item/<int:pk>/', ItemDetailView.as_view(), name='item-detail'),
    # path('category/<slug:category_slug_items>', show_category_items)
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
