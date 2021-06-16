from django.db import models


class EstateType(models.Model):
    title = models.CharField('Название', max_length=100)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Вид недвижимости'
        verbose_name_plural = 'Виды недвижимости'


class Estate(models.Model):
    title = models.CharField('Название', default="",  max_length=100)
    address = models.CharField('Адрес', default="", max_length=1000)
    surface_area = models.FloatField('Площадь', default=0,  blank=True)
    price = models.FloatField('Цена', default=1000000)
    text = models.TextField('Описание', default="", max_length=50000)
    type = models.ForeignKey(EstateType, default="", verbose_name="Тип", on_delete=models.CASCADE)
    photo_path = models.CharField('Путь до фото', default="", max_length=100, blank=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Недвижимость'
        verbose_name_plural = 'Объекты недвижимости'
