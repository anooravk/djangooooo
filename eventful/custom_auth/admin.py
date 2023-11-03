from django.contrib import admin
from .models import User


class EventsUser(admin.ModelAdmin):
    list_display = ('username', 'email', 'last_login', 'date_joined', 'is_superuser', 'ishost', 'is_staff', 'is_active')
    list_filter = ('last_login', 'date_joined', 'is_superuser','ishost','is_staff','is_active') 
    search_fields = ['username','email']

admin.site.register(User,EventsUser)




