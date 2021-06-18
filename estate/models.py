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
    estate_type = models.ForeignKey(EstateType, default="", verbose_name="Тип", on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Недвижимость'
        verbose_name_plural = 'Объекты недвижимости'


class Gallery(models.Model):
    image = models.ImageField(upload_to='gallery')
    estate = models.ForeignKey(Estate, on_delete=models.CASCADE, related_name='images')

    def __str__(self):
        return self.image.name

    class Meta:
        verbose_name = 'Галерея'
        verbose_name_plural = 'Галереи'