from django.contrib import admin

from core.models import User
from organizations.models import Organization


class UserInLine(admin.TabularInline):
    """
    Class representing user inline block
    """
    model = User
    fields = ['email']
    readonly_fields = ['email']
    extra = 0


@admin.register(Organization)
class OrganizationAdmin(admin.ModelAdmin):
    """
    Class representing event admin

    Attrs:
        - list_display: defines collection of fields to display
        - search_fields: defines collection of fields to search
        - inlines: defines UserInLine
        - fieldsets: defines custom subsections
    """
    list_display = ('title', 'description', 'address', 'postcode')
    search_fields = ('title',)
    inlines = [UserInLine]

    fieldsets = (
        ('Информация', {
            'fields': ('title', 'description')
        }),
        ('Полный адрес', {
            'fields': ('address', 'postcode')
        }),
    )
