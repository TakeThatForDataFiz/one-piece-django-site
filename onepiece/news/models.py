from django.db import models

# Create your models here.


class Manga(models.Model):
    name = models.CharField(max_length=200)
    plot_summary = models.TextField()
    genres = models.ArrayField(
        models.CharField(max_length=25, blank=True),
        size=4
    ),
    themes = models.ArrayField(
        models.CharField(max_length=25, blank=True),
        size=3),
    official_website = models.CharField(max_length=400)
    images = models.ArrayField(
        models.ImageField(),
        size=4),
    author = models.CharField(max_length=200)


class Anime(models.Model):
    name = models.CharField(max_length=200)
    plot_summary = models.TextField()
    genres = models.ArrayField(
        models.CharField(max_length=25, blank=True),
        size=4
    ),
    themes = models.ArrayField(
        models.CharField(max_length=25, blank=True),
        size=3),
    official_website = models.CharField(max_length=400)
    images = models.ArrayField(
        models.ImageField(),
        size=4)
    company = models.CharField(max_length=200)


class Article(models.Model):
    title = models.CharField(max_length=400)
    release_date = models.DateField()
    link = models.CharField(max_length=1000)


class Episode(models.Model):
    arc = models.CharField(max_length=400)
    title = models.CharField(max_length=200)
    number = models.IntegerField()
    is_canon = models.BooleanField()
    air_date = models.DateField()


class Chapter(models.Model):
    # Note -- Will need to Scrape and parse HTML incoming from ANN to get chapter details
    arc = models.CharField(max_length=400)
    title = models.CharField(max_length=400)
    number = models.IntegerField()
    release_date = models.DateField()
