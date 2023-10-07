from django.db import models

class Workers(models.Model):

    name = models.CharField(max_length=255, verbose_name='Имя работника')
    phone_number = models.CharField(max_length=255, verbose_name='Телефон работника')

    class Meta:
        verbose_name = 'Работник'
        verbose_name_plural = 'Работники'

    def __str__(self):
        return self.name


class A_Stores(models.Model):

    name = models.CharField(max_length=255, verbose_name='Название торговой точки')
    worker = models.ForeignKey(Workers, on_delete=models.CASCADE, related_name='a_stores', verbose_name='Работник')

    class Meta:
        verbose_name = 'Торговая точка'
        verbose_name_plural = "Торговые точки"

    def __str__(self):
        return self.name
