from django.db import models

# Create your models here.


class Items(models.Model):

    name = models.CharField(verbose_name='Название', max_length=256, blank=False)
    created_at = models.DateField(verbose_name='Дата поступления', auto_now_add=True)
    unit = models.CharField(verbose_name='Единица измерения', max_length=128)
    price = models.DecimalField(verbose_name='Цена', max_digits=8, decimal_places=0, default=0)
    vendor = models.CharField(verbose_name='Имя поставщика', max_length=128)

    def __str__(self):
        return self.name
