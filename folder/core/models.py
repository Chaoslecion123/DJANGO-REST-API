from django.db import models

# Create your models here.
class portafolio(models.Model):
    title = models.CharField(max_length = 200, verbose_name="titulo")
    description = models.TextField(verbose_name="descripcion")
    langs = models.CharField(max_length =200, verbose_name="lenguaje")
    created = models.DateTimeField(auto_now_add=True,verbose_name='fecha de creacion')
    updated = models.DateTimeField(auto_now=True, verbose_name='fecha de actualizacion')

    class Meta:
        verbose_name='portafolio'
        verbose_name_plural = 'portafolios'
        ordering = ['-created']


    def __str__(self):
        return  self.title

