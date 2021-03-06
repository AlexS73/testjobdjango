# Generated by Django 3.0.2 on 2020-05-20 07:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('darkside', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='correctanswer',
            field=models.BooleanField(default=False, verbose_name='Правильный ответ'),
        ),
        migrations.AlterField(
            model_name='test',
            name='uidorden',
            field=models.IntegerField(verbose_name='Уникальный код ордена'),
        ),
    ]
