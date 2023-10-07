from django.db import models

from a_store.models import A_Stores

class Visits(models.Model):

    a_store = models.ForeignKey(A_Stores, on_delete=models.PROTECT, related_name='a_store', verbose_name='Торговая точка')
    data = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    latitude = models.FloatField(verbose_name='Широта')
    longitude = models.FloatField(verbose_name='Долгота')

    class Meta:
        verbose_name = 'Посещение'
        verbose_name_plural = 'Посещения'

    def __str__(self):
        return self.a_store.name