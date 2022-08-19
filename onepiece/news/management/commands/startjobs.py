from django.core.management.base import BaseCommand
from dateutil import parser
from bs4 import BeautifulSoup
import requests


class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        # Get manga details via API
        tags = get_bs4_soup()
        parse_manga_information(tags)

    def get_bs4_soup(self):
        res = requests.get(
            "https://cdn.animenewsnetwork.com/encyclopedia/api.xml?manga=1223")
        tags = BeautifulSoup(res.content, 'lxml-xml')
        return tags

    def parse_manga_information(self, tags):
        # parse manga xml information and return as unpacked tuple
        name = tags.manga['name']
        des = tags.find(type='Plot Summary').contents[0]
        return (name, des)
