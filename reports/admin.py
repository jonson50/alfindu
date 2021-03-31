from django.contrib import admin
from .models import ReportType, Report


class ReportTypeAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')
    list_display = ('name', 'reference')


class ReportsAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')
    list_display = ('name', 'report_type', 'component', 'office', 'inspection_date', 'next_inspection_date')


admin.site.register(ReportType, ReportTypeAdmin)
admin.site.register(Report, ReportsAdmin)
