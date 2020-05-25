# Generated by Django 3.0.2 on 2020-05-23 04:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('darkside', '0002_auto_20200520_1059'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='question',
            name='correctanswer',
        ),
        migrations.RemoveField(
            model_name='resulttest',
            name='test',
        ),
        migrations.AlterField(
            model_name='resulttest',
            name='question',
            field=models.CharField(max_length=500, verbose_name='Вопрос'),
        ),
        migrations.AlterField(
            model_name='test',
            name='uidorden',
            field=models.IntegerField(unique=True, verbose_name='Уникальный код ордена'),
        ),
    ]
