from django.db import models
from django import forms

# Create your models here.
class Planet(models.Model):
    name = models.CharField(max_length=50, verbose_name='Название планеты')

    class Meta:
        verbose_name_plural = 'Планеты'
        verbose_name = 'Планета'
    def __str__(self):
        return self.name

class Recruit(models.Model):
    name = models.CharField(max_length=50, verbose_name='Имя')
    planet = models.ForeignKey(Planet, on_delete= models.CASCADE, verbose_name='Планета обитания')
    email = models.EmailField(verbose_name='Электронная почта')
    age = models.SmallIntegerField(verbose_name='Возраст')
    handshadow = models.ForeignKey('Sith', on_delete=models.CASCADE, null=True, verbose_name='Рука тени')

    class Meta:
        verbose_name = 'Рекрут'
        verbose_name_plural = 'Рекруты'

    def __str__(self):
        return self.name

class Sith(models.Model):
    name = models.CharField(max_length=50, verbose_name='Имя')
    planet = models.ForeignKey(Planet, on_delete=models.CASCADE, verbose_name='Планета обучения')

    class Meta:
        verbose_name = 'Ситх'
        verbose_name_plural = 'Ситхи'

    def __str__(self):
        return self.name

class Test(models.Model):
    uidorden = models.IntegerField(unique=True, verbose_name='Уникальный код ордена')

    class Meta:
        verbose_name = 'Тест'
        verbose_name_plural = 'Тесты'

    def __str__(self):
        return str(self.uidorden)

class Question(models.Model):
    text = models.CharField(max_length=500,verbose_name='Вопрос')
    test = models.ForeignKey(Test, on_delete=models.CASCADE, verbose_name='Тест')

    class Meta:
        verbose_name = 'Вопрос'
        verbose_name_plural = 'Вопросы'

    def __str__(self):
        return self.text

class ResultTest(models.Model):
    recruit = models.ForeignKey(Recruit, on_delete=models.CASCADE, verbose_name='Рекрут')
    question = models.CharField(max_length=500, default='',verbose_name='Вопрос')
    choise = models.CharField(max_length=50,default='', verbose_name='Ответ')

    class Meta:
        verbose_name = 'Результаты теста'
        verbose_name_plural = 'Результаты тестов'






















