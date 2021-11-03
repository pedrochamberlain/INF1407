from django.db import models

# Create your models here.


class Filme(models.Model):

    title = models.CharField(
        max_length=100, verbose_name='Título do filme')
    year_of_release = models.IntegerField(
        verbose_name='Ano de lançamento do filme')
    director = models.CharField(verbose_name='Diretor do filme', max_length=30)
    genre = models.CharField(verbose_name='Gênero do filme', max_length=30)
    country = models.CharField(verbose_name='País de origem', max_length=30)
    runtime = models.IntegerField(verbose_name='Duração do filme')

    def __str__(self):
        return self.title
