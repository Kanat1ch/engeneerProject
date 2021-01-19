from django.db import models


class Marks(models.Model):
    mark = models.CharField(max_length=20, db_index=True, verbose_name='Марка')
    model = models.CharField(max_length=20, db_index=True, verbose_name='Модель')

    def __str__(self):
        return self.mark + ' ' + self.model

    class Meta:
        verbose_name_plural = 'Модельный ряд'
        verbose_name = 'Модельный ряд'
        ordering = ['mark']


class Type(models.Model):
    name = models.CharField(max_length=20, db_index=True, verbose_name='Типы')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Типы'
        verbose_name = 'Тип'
        ordering = ['name']

class Wheels(models.Model):
    mark = models.CharField(max_length=20, db_index=True, verbose_name='Марка')
    model = models.CharField(max_length=20, db_index=True, verbose_name='Модель')
    diameter = models.FloatField(null=True, blank=True, verbose_name='Диаметр')

    def __str__(self):
        return self.mark + ' ' + self.model + ' ' + str(self.diameter)

    class Meta:
        verbose_name_plural = 'Колёса'
        verbose_name = 'Колёса'
        ordering = ['mark']


class Bsles(models.Model):
    stamp = models.ForeignKey('Marks', null=True, on_delete=models.PROTECT, verbose_name='Бренд')
    type = models.ForeignKey('Type', null=True, on_delete=models.PROTECT, verbose_name='Тип')
    wheels = models.ForeignKey('Wheels', null=True, on_delete=models.PROTECT, verbose_name='Колеса')
    weight = models.FloatField(null=True, blank=True, verbose_name='Вес')
    price = models.FloatField(null=True, blank=True, verbose_name='Цена')

    class Meta:
        verbose_name_plural = 'Велосипеды'
        verbose_name = 'Велосипед'
        ordering = ['stamp']
