from django.contrib import admin
from .models import Customer, Office


class CustomerAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')
    list_display = ('name', 'document_type', 'document_number', 'email', 'is_active', 'created')


class OfficeAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')
    list_display = ('name', 'customer', 'is_active', 'created')


admin.site.register(Customer, CustomerAdmin)
admin.site.register(Office, OfficeAdmin)
