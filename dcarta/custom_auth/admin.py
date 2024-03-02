from django.contrib import admin
from .models import User
from django.contrib.auth.admin import UserAdmin
from .models import UserProfile
from django.utils.translation import gettext_lazy as _
from django.contrib.auth import get_user_model
from .models import UserProfile

class DcartaUser(admin.ModelAdmin):
    list_display = ('username', 'email', 'last_login', 'date_joined', 'is_superuser', 'is_staff', 'is_active')
    list_filter = ('last_login', 'date_joined', 'is_superuser','is_staff','is_active') 
    search_fields = ['username','email']

admin.site.register(User,DcartaUser)
admin.site.register(UserProfile)


class UserProfileInline(admin.StackedInline):
    model = UserProfile
    can_delete = False
    verbose_name_plural = _('User Profiles')

class CustomUserAdmin(UserAdmin):
    inlines = (UserProfileInline,)


admin.site.unregister(get_user_model())


admin.site.register(get_user_model(), CustomUserAdmin)


