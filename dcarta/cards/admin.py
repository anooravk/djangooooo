from django.contrib import admin
from .models import BusniessCards
from django.contrib.auth.models import Group



class CardsAdmin(admin.ModelAdmin):
    list_display = ('fullName', 'emailAddress', 'contactNumber', 'companyName', 'address','jobTitle','exchangers')
    list_filter = ('companyName', 'jobTitle','emailAddress') 
    search_fields = ['companyName','fullName']

    


admin.site.unregister(Group)

admin.site.register(BusniessCards, CardsAdmin)




