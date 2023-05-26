from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from core.models import User


# ----------------------------------------------------------------
from django.contrib import admin

from core.models import User


# ----------------------------------------------------------------
# admin register
@admin.register(User)
class CustomUserAdmin(admin.ModelAdmin):
    """
    Model representing a user admin

    Attrs:
        - model: User model
        - list_display: defines collection of fields to display
        - search_fields: defines collection of fields to search
        - exclude: defines fields to be hidden
        - readonly_fields: defines fields only to read
    """
    model = User
    list_display = ('email',)
    search_fields = ('email',)
    exclude = ('password', 'last_login')
