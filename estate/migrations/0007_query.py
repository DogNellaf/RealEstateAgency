# Generated by Django 3.1.1 on 2021-06-21 22:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('estate', '0006_auto_20210618_1327'),
    ]

    operations = [
        migrations.CreateModel(
            name='Query',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=100, verbose_name='Имя')),
                ('mobile', models.CharField(default='', max_length=100, verbose_name='Имя')),
                ('sell', models.BooleanField(blank=True, default=False, verbose_name='Продать недвижимость')),
                ('legalization', models.BooleanField(blank=True, default=False, verbose_name='Оформление')),
                ('buy', models.BooleanField(blank=True, default=False, verbose_name='Купить недвижимость')),
                ('cadastre', models.BooleanField(blank=True, default=False, verbose_name='Кадастровые услуги')),
                ('rent', models.BooleanField(blank=True, default=False, verbose_name='Сдать недвижимость')),
                ('juridical', models.BooleanField(blank=True, default=False, verbose_name='Юридическое сопровождение')),
                ('other', models.TextField(blank=True, default='', max_length=50000, verbose_name='Другой вопрос')),
            ],
            options={
                'verbose_name': 'Заявка',
                'verbose_name_plural': 'Заявки',
            },
        ),
    ]