from django.db import models

class Dictionary(models.Model):
    title = models.CharField(max_length=36, verbose_name='Заголовок')
    description = models.CharField(max_length=300, verbose_name='Описание')
    image = models.ImageField(upload_to='%Y/%m/%d', blank=True, null=True, verbose_name='Изображение')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Словарь'
        verbose_name_plural = 'Словари'
