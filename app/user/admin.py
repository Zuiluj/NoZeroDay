from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin

from .forms import LoginUserForm, CreateUserForm, CustomUserChange
from .models import User
# Register your models here.

class CustomUserAdmin(UserAdmin):
    model = User
    add_form = CreateUserForm 
    form = CustomUserChange
    readonly_fields = ('date_joined',)
    list_display = ['email', 'name', 'username', ]
    list_filter = ['email', 'name', 'username']
    
    # add the custom fieldsets proportionate to what the (Custom) User have
    add_fieldsets = UserAdmin.add_fieldsets + (
        (
            None,
            {
                'classes': ('wide',),
                'fields': ('name', 'email'),
            },
        ),
    )

admin.site.register(User, CustomUserAdmin)