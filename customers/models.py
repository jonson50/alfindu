from django.db import models
# from django.conf import settings


class Customer(models.Model):
    name = models.CharField(verbose_name='nombre', max_length=200)
    email = models.EmailField(max_length=254)
    telephone = models.CharField(verbose_name='telefono', max_length=12)
    document_type = models.CharField(verbose_name='tipo de documento', max_length=4)
    document_number = models.IntegerField(verbose_name='numero de documento')
    contact = models.CharField(verbose_name='contacto', max_length=200)
    is_active = models.BooleanField(verbose_name='activo', default=True)
    created = models.DateTimeField(verbose_name='creado', auto_now_add=True)
    updated = models.DateTimeField(verbose_name='actualizado', auto_now=True)

    class Meta:
        verbose_name = 'cliente'
        verbose_name_plural = 'clientes'
        ordering = ['-created']

    def __str__(self):
        return self.name


class Office(models.Model):
    # accounts = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, verbose_name='cliente')
    name = models.CharField(max_length=200, verbose_name='nombre')
    is_active = models.BooleanField(default=True, verbose_name='activo')
    created = models.DateTimeField(auto_now_add=True, verbose_name='creado')
    updated = models.DateTimeField(auto_now=True, verbose_name='actualizado')

    class Meta:
        verbose_name = 'oficina'
        verbose_name_plural = 'oficinas'
        ordering = ['customer', 'name']

    def __str__(self):
        return self.name + ' - ' + str(self.customer)
