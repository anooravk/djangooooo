from django.contrib import admin
from .models import Event,Category,User
from django.contrib.auth.models import Group



class EventsAdmin(admin.ModelAdmin):
    list_display = ('eventName', 'description', 'location', 'status', 'category')
    list_filter = ('status', 'location', 'category__categoryName','startDate','endDate') 
    search_fields = ['eventName']

    def category_name(self, obj):
        return obj.category.categoryName
    

class EventsUser(admin.ModelAdmin):
    list_display = ('username', 'email', 'last_login', 'date_joined', 'is_superuser', 'isHost', 'is_staff', 'is_active')
    list_filter = ('last_login', 'date_joined', 'is_superuser','isHost','is_staff','is_active') 
    search_fields = ['username','email']


admin.site.unregister(Group)

admin.site.register(Event, EventsAdmin)
admin.site.register(Category)
admin.site.register(User,EventsUser)


