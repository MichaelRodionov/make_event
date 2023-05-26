from django.contrib import admin
from django.utils.safestring import mark_safe

from events.models import Event


class OrganizationInline(admin.TabularInline):
    """
    Class representing organization inline block
    """
    model = Event.organizations.through
    extra = 0
    verbose_name_plural = 'Организации'


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    """
    Class representing event admin

    Attrs:
        - list_display: defines collection of fields to display
        - search_fields: defines collection of fields to search
        - inlines: defines OrganizationInline
        - list_filter: defines collection of fields to filter
        - readonly_fields: defines fields only to read
        - fieldsets: defines custom subsections
    """
    list_display = ('title', 'description', 'preview', 'date')
    search_fields = ('title', 'date')
    inlines = [OrganizationInline]
    list_filter = ('title', 'date')
    readonly_fields = ('preview',)

    fieldsets = (
        ('Информация', {
            'fields': ('title', 'description')
        }),
        ('Дата', {
            'fields': ('date',)
        }),
        ('Логотип', {
            'fields': ('image', 'preview')
        })
    )

    def preview(self, obj):
        """
        Method to get preview of event picture
        """
        if obj.image:
            return mark_safe(f'<img src="{obj.image.url}" width="120" height="120" />')
        else:
            return None

    preview.short_description = 'Предпросмотр'
