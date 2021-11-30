from django.db import models
from django.db.models.fields import URLField

# Create your models here.

class Tutorial(models.Model):
    titulo=models.CharField(max_length=50)
    url=models.CharField(max_length=50)
    imagen=models.ImageField(upload_to='tutoriales')
    created=models.DateTimeField(auto_now_add=True) 
    updated=models.DateTimeField(auto_now_add=True) 

    class Meta:
        verbose_name='tutorial'
        verbose_name_plural='tutoriales'

    def __str__(self):
        return self.titulo