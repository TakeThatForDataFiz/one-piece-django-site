from django.contrib import admin
from .models import Manga, Anime, Episode, Article, Chapter

# Register your models here.
admin.site.register(Manga)
admin.site.register(Anime)
admin.site.register(Episode)
admin.site.register(Article)
admin.site.register(Chapter)
