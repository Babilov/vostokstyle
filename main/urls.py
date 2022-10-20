from django.contrib import admin
from django.urls import path, include
from .views import ItemListView, ItemDetailView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', ItemListView.as_view(), name='home'),
    path('item/<int:pk>/', ItemDetailView.as_view(), name='item-detail')
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
