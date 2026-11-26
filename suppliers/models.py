from django.db import models
from .validators import validate_cnpj



class Supplier(models.Model):
    name = models.CharField(max_length=300)

    cnpj = models.CharField(
        max_length=18,
        unique=True,
        validators=[validate_cnpj]
        )

    phone = models.CharField(max_length=20)

    email = models.EmailField()


    class Meta:
        ordering = ['name']


    def __str__(self):
        return self.name

