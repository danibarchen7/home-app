from django.contrib import admin
from Customer.models import Customers
# Register your models here.
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import *
# Register your models here


class UsersAdmin(UserAdmin):
    list_display = (
        'username', 'email', 'user_type', 'first_name', 'last_name', 'phone',
        'is_staff', 'is_superuser', 'is_active'
    )

    fieldsets = (
        (None, {
            'fields': ('username', 'password', 'user_type',)
        }),
        ('Personal info', {
            'fields': ('first_name', 'last_name', 'email', 'phone')
        }),
        ('Permissions', {
            'fields': (
                'is_active', 'is_staff', 'is_superuser',
                'groups', 'user_permissions'
            )
        }),
        ('Important dates', {
            'fields': ('last_login', 'date_joined')
        })
    )

    add_fieldsets = (
        (None, {
            'fields': ('username', 'password1', 'password2')
        }),
        ('Personal info', {
            'fields': ('first_name', 'last_name', 'email', 'phone', 'user_type',)
        }),
        ('Permissions', {
            'fields': (
                'is_active', 'is_staff', 'is_superuser',
                'groups', 'user_permissions'
            )
        }),
        ('Important dates', {
            'fields': ('last_login', 'date_joined')
        })
    )


admin.site.register(Customers,UsersAdmin)