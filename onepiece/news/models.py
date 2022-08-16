from django.db import models
from django.contrib.postgres.fields import ArrayField
# Create your models here.


class Manga(models.Model):
    name = models.CharField(max_length=200)
    plot_summary = models.TextField()
    genres = ArrayField(
        models.CharField(max_length=25, blank=True),
        size=4
    ),
    themes = ArrayField(
        models.CharField(max_length=25, blank=True),
        size=3),
    official_website = models.CharField(max_length=400)
    images = ArrayField(
        models.ImageField(),
        size=4),
    author = models.CharField(max_length=200)

    def __str__(self):
        return f'{self.name} - {self.plot_summary} - written by {self.author}'


class Anime(models.Model):
    name = models.CharField(max_length=200)
    plot_summary = models.TextField()
    genres = ArrayField(
        models.CharField(max_length=25, blank=True),
        size=4
    ),
    themes = ArrayField(
        models.CharField(max_length=25, blank=True),
        size=3),
    official_website = models.CharField(max_length=400)
    images = ArrayField(
        models.ImageField(),
        size=4)
    company = models.CharField(max_length=200)

    def __str__(self):
        return f'{self.name} - {self.plot_summary} created by {self.company}'


class Article(models.Model):
    title = models.CharField(max_length=400)
    release_date = models.DateField()
    link = models.CharField(max_length=1000)

    def __str__(self):
        return f'{self.title} released on {self.release_date}'


class Episode(models.Model):
    arc = models.CharField(max_length=400)
    title = models.CharField(max_length=200)
    number = models.IntegerField()
    is_canon = models.BooleanField()
    air_date = models.DateField()

    def __str__(self):
        return f'Episode: {self.number} - {self.title} - Released: {self.air_date}'


class Chapter(models.Model):
    # Note -- Will need to Scrape and parse HTML incoming from ANN to get chapter details
    arc = models.CharField(max_length=400)
    title = models.CharField(max_length=400)
    number = models.IntegerField()
    release_date = models.DateField()

    def __str__(self):
        return f'Chapter: {self.number} - {self.title} - Released: {self.realease_date}'
