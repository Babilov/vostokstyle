from django.contrib import admin
from .models import Burner, Category, AllItems, Heater, Images, Order


class AdminAllItems(admin.ModelAdmin):
    exclude = ('name_lower', )


admin.site.register(Burner)
admin.site.register(Heater)
admin.site.register(Category)
admin.site.register(AllItems, AdminAllItems)
admin.site.register(Images)
admin.site.register(Order)
