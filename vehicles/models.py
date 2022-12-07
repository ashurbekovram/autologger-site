from django.db import models


class Country(models.Model):
    name = models.CharField(max_length=255, verbose_name='Наименование')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Страна'
        verbose_name_plural = 'Страны'
        ordering = ['name']


class Brand(models.Model):
    name = models.CharField(max_length=255, verbose_name='Наименование')
    description = models.TextField(verbose_name='Описание')
    founding_date = models.DateField(verbose_name='Дата основания')
    country = models.ForeignKey('Country', on_delete=models.PROTECT, verbose_name='Страна')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Бренд'
        verbose_name_plural = 'Бренды'
        ordering = ['name']


class Series(models.Model):
    name = models.CharField(max_length=255, verbose_name='Наименование')
    brand = models.ForeignKey('Brand', on_delete=models.PROTECT, verbose_name='Бренд', related_name='series')

    def __str__(self):
        return self.brand.name + " " + self.name

    class Meta:
        verbose_name = 'Серия'
        verbose_name_plural = 'Серии'


class Generation(models.Model):
    name = models.CharField(max_length=255, verbose_name='Наименование')
    start_year = models.PositiveIntegerField(verbose_name='Начало производства')
    end_year = models.PositiveIntegerField(verbose_name='Конец производства')
    series = models.ForeignKey('Series', on_delete=models.PROTECT, verbose_name='Серия')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Поколение'
        verbose_name_plural = 'Поколения'
