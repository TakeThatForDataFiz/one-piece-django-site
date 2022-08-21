from django.core.management.base import BaseCommand
from dateutil import parser
from bs4 import BeautifulSoup
from models import Manga
import requests


class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        # Get manga details via API
        tags = get_bs4_soup()
        name, des, author = parse_manga_information(tags)
        if not Manga.objects.filter(name="One Piece").exists():
            manga = Manga(name=name, plot_summary=des, author=author)
            manga.save()


def get_bs4_soup():
    res = requests.get(
        "https://cdn.animenewsnetwork.com/encyclopedia/api.xml?manga=1223")
    tags = BeautifulSoup(res.content, 'lxml-xml')
    return tags


def parse_manga_information(tags):
    # parse manga xml information and return as unpacked tuple
    name = tags.manga['name']
    des = tags.find(type='Plot Summary').contents[0]
    author = tags.person.contents[0]
    return (name, des, author)
