from django.db import models
from django.contrib.auth import get_user_model


User = get_user_model()


class Artiles(models.Model):
    CATEGORY_CHOICES = [
        ('animals', 'Животные'),
        ('people', 'Люди'),
        ('food', 'Еда'),
        ('other', 'Другое'),
    ]

    title = models.CharField('Название', max_length=100, default='Без названия')
    anons = models.CharField('Анонс', max_length=250)
    full_text = models.TextField('Статья')
    date = models.DateTimeField('Дата публикации')
    category = models.CharField('Категория', max_length=20, choices=CATEGORY_CHOICES, default='other')

    def __str__(self):
        return f'Новость: {self.title}'

    def get_absolute_url(self):
        return f'/news/{self.id}'

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'


class Comment(models.Model):
    article = models.ForeignKey(Artiles, on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField('Текст комментария')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Комментарий от {self.author.username}'
