from django.db import models


class Transmissions(models.Model):
    name = models.CharField(max_length=20, db_index=True, verbose_name='Коробки передач')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Коробки передач'
        verbose_name = 'Коробка передач'
        ordering = ['name']


class Marks(models.Model):
    mark = models.CharField(max_length=20, db_index=True, verbose_name='Марка')
    model = models.CharField(max_length=20, db_index=True, verbose_name='Модель')

    def __str__(self):
        return self.mark + ' ' + self.model

    class Meta:
        verbose_name_plural = 'Модельный ряд'
        verbose_name = 'Модельный ряд'
        ordering = ['mark']


class Ranks(models.Model):
    rank = models.CharField(max_length=20, db_index=True, verbose_name='Класс')

    def __str__(self):
        return self.rank

    class Meta:
        verbose_name_plural = 'Классы'
        verbose_name = 'Класс'
        ordering = ['rank']

class Cars(models.Model):
    stamp = models.ForeignKey('Marks', null=True, on_delete=models.PROTECT, verbose_name='Модельный ряд')
    price = models.FloatField(null=True, blank=True, verbose_name='Цена')
    release = models.DateField(null=True, blank=True, verbose_name='Дата выпуска')
    transmission = models.ForeignKey('Transmissions', null=True, on_delete=models.PROTECT, verbose_name='Коробка передач')
    rank = models.ForeignKey('Ranks', null=True, on_delete=models.PROTECT, verbose_name='Класс')

    class Meta:
        verbose_name_plural = 'Автомобили'
        verbose_name = 'Автомобиль'
        ordering = ['stamp']



