from django.contrib import admin
from .models import Burner, Category, AllItems


class BurnerAdmin(admin.ModelAdmin):
    exclude = ('category', )


admin.site.register(Burner, BurnerAdmin)
admin.site.register(Category)
admin.site.register(AllItems)
