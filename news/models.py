from django.db import models

class Articles(models.Model):
    title = models.CharField('Название', max_length=50)
    full_text = models.TextField('Рецепт')
    date = models.DateTimeField('Дата публикации')



    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'