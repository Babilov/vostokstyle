from django.contrib import admin
from .models import Burner, Category, AllItems, Heater, Images


admin.site.register(Burner)
admin.site.register(Heater)
admin.site.register(Category)
admin.site.register(AllItems)
admin.site.register(Images)
