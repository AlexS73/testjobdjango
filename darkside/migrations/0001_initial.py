# Generated by Django 3.0.2 on 2020-05-20 07:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Planet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Название планеты')),
            ],
            options={
                'verbose_name': 'Планета',
                'verbose_name_plural': 'Планеты',
            },
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=500, verbose_name='Вопрос')),
                ('correctanswer', models.BooleanField(default=False, verbose_name='Ответы')),
            ],
            options={
                'verbose_name': 'Вопрос',
                'verbose_name_plural': 'Вопросы',
            },
        ),
        migrations.CreateModel(
            name='Recruit',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Имя')),
                ('email', models.EmailField(max_length=254, verbose_name='Электронная почта')),
                ('age', models.SmallIntegerField(verbose_name='Возраст')),
            ],
            options={
                'verbose_name': 'Рекрут',
                'verbose_name_plural': 'Рекруты',
            },
        ),
        migrations.CreateModel(
            name='Test',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uidorden', models.IntegerField(unique=True, verbose_name='Уникальный код ордена')),
            ],
            options={
                'verbose_name': 'Тест',
                'verbose_name_plural': 'Тесты',
            },
        ),
        migrations.CreateModel(
            name='Sith',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Имя')),
                ('planet', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='darkside.Planet', verbose_name='Планета обучения')),
            ],
            options={
                'verbose_name': 'Ситх',
                'verbose_name_plural': 'Ситхи',
            },
        ),
        migrations.CreateModel(
            name='ResultTest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('result', models.BooleanField(default=False, verbose_name='Результат ответа')),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='darkside.Question', verbose_name='Вопрос')),
                ('recruit', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='darkside.Recruit', verbose_name='Рекрут')),
                ('test', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='darkside.Test', verbose_name='Тест')),
            ],
            options={
                'verbose_name': 'Результат теста',
                'verbose_name_plural': 'Результаты тестов',
            },
        ),
        migrations.AddField(
            model_name='recruit',
            name='handshadow',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='darkside.Sith', verbose_name='Рука тени'),
        ),
        migrations.AddField(
            model_name='recruit',
            name='planet',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='darkside.Planet', verbose_name='Планета обитания'),
        ),
        migrations.AddField(
            model_name='question',
            name='test',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='darkside.Test', verbose_name='Тест'),
        ),
    ]
