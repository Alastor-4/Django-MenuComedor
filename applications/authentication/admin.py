from django.contrib import admin

from .models import User


class UserAdmin(admin.ModelAdmin):
    list_display = ("username", "email", "codregistro", "is_staff", "is_active")
    exclude = ("groups", "last_login", "user_permissions", "password")


admin.site.register(User, UserAdmin)
