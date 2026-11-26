from django.db import models
import re
from django.core.exceptions import ValidationError



#VALIDAÇÃO DE CPF DE PRIMEIRA:
def validate_cpf(value):
    cpf = re.sub(r'\D', '', value)

    if len(cpf) != 11:
        raise ValidationError('O CPF deve conter 11 dígitos.')

    if cpf == cpf[0] * 11:
        raise ValidationError('CPF inválido.')

    for position in (9, 10):
        weight = position + 1
        total = sum(
            int(digit) * (weight - index)
            for index, digit in enumerate(cpf[:position])
        )

        remainder = (total * 10) % 11
        digit = 0 if remainder == 10 else remainder

        if digit != int(cpf[position]):
            raise ValidationError('CPF inválido.')




#MODELS COMPLETO:

PLAN_CHOICES = [
    ('monthly', 'Mensal'),
    ('quarterly', 'Trimensal'),
    ('annual', 'Anual')
]


class Athlete(models.Model):
    name = models.CharField(max_length=500)
    cpf = models.CharField(
        max_length=14,
        unique=True,
        validators=[validate_cpf]
        )

    email = models.EmailField(max_length=254, blank=True, null=True)
    phone = models.CharField(max_length=30, blank=True, null=True)
    birth_date = models.DateField(blank=True, null=True)
    enrollment = models.DateField(auto_now_add=True)
    status = models.CharField(
        max_length=20,
        choices=[
            ('active', 'Ativo'),
            ('inactive', 'Inativo'),
                              ],
        default='active')

    plan = models.CharField(
        max_length=10,
        choices=PLAN_CHOICES,
        default='monthly'
          )

    observations = models.TextField(blank=True, null=True)


    class Meta:
        ordering = ['name']


    def __str__(self):
        return self.name





    




