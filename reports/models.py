from django.db import models
from customers.models import Office
from django.conf import settings
import os


class ReportType(models.Model):
    name = models.CharField(max_length=50, verbose_name='tipo de reporte')
    reference = models.CharField(max_length=20, verbose_name='referencia')
    created = models.DateTimeField(auto_now_add=True, verbose_name='creado')
    updated = models.DateTimeField(auto_now=True, verbose_name='actualizado')

    class Meta:
        verbose_name = 'tipo de reporte'
        verbose_name_plural = 'tipos de reporte'
        ordering = ['name']

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.name = self.name.upper()
        self.reference = self.reference.upper()
        return super(ReportType, self).save(*args, **kwargs)

def get_document_filepath(self, filename):
    return f'documents/reports/{self.office.customer}/{self.office.name}/{filename}'


class Report(models.Model):
    name = models.CharField(max_length=200, verbose_name='Reporte')
    report_type = models.ForeignKey(ReportType, on_delete=models.CASCADE,
                                    verbose_name='tipo de reporte')
    office = models.ForeignKey(Office, on_delete=models.CASCADE, verbose_name='Oficina')
    reference = models.CharField(max_length=50, verbose_name='referencia')
    component = models.CharField(max_length=200, verbose_name='componente')
    document = models.FileField(upload_to=get_document_filepath, verbose_name='documento')
    inspection_date = models.DateField(verbose_name='fecha de inspeccion')
    next_inspection_date = models.DateField(verbose_name='fecha de proxima inspeccion')
    created = models.DateTimeField(auto_now_add=True, verbose_name='creado')
    updated = models.DateTimeField(auto_now=True, verbose_name='actualizado')

    class Meta:
        verbose_name = 'reporte'
        verbose_name_plural = 'reportes'
        ordering = ['-created', 'office']

    def __str__(self):
        return self.name + ' - ' + str(self.office)

    def get_document_filename(self):
        #file = str(self.document)[str(self.document).index(f'documents/reports/{self.office.customer}/{self.office.name}/'):]
        file = str(self.document)
        return os.path.join(settings.MEDIA_ROOT, file)

    def save(self, *args, **kwargs):
        self.name = self.name.upper()
        self.reference = self.reference.upper()
        self.component = self.component.upper()
        return super(Report, self).save(*args, **kwargs)
