# Generated by Django 3.0.2 on 2020-05-24 15:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('darkside', '0003_auto_20200523_0716'),
    ]

    operations = [
        migrations.CreateModel(
            name='ResultTestTwo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('recruit', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='darkside.Recruit', verbose_name='Рекрут')),
            ],
        ),
    ]
