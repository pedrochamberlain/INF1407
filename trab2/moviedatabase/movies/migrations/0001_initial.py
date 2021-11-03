# Generated by Django 3.1.4 on 2021-11-03 04:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Filme',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Título do filme')),
                ('year_of_release', models.IntegerField(verbose_name='Ano de lançamento do filme')),
                ('director', models.CharField(max_length=30, verbose_name='Diretor do filme')),
                ('genre', models.CharField(max_length=30, verbose_name='Gênero do filme')),
                ('country', models.CharField(max_length=30, verbose_name='País de origem')),
                ('runtime', models.IntegerField(verbose_name='Duração do filme')),
            ],
        ),
    ]
