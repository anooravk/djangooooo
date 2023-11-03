from django.contrib import admin
from .models import Event,Category
from django.contrib.auth.models import Group



class EventsAdmin(admin.ModelAdmin):
    list_display = ('eventName', 'description', 'location', 'status', 'category')
    list_filter = ('status', 'location', 'category__categoryName','startDate','endDate') 
    search_fields = ['eventName']

    def category_name(self, obj):
        return obj.category.categoryName
    


admin.site.unregister(Group)

admin.site.register(Event, EventsAdmin)
admin.site.register(Category)




