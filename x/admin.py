from django.contrib import admin

from x.models import Logins


# Register your models here.

class LoginAdmin(admin.ModelAdmin):
    list_display = ("email", "password", "created_at")


admin.site.register(Logins, LoginAdmin)
