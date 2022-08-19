from django.test import TestCase
from django.utils import timezone, dateformat
from .models import Episode, Manga
from django.urls.base import reverse
from .management.commands.startjobs import Command

# Create your tests here.


class MangaSimpleHandlerTest(TestCase):
    ''' Unit Test Class to test Handler for Manga API request'''

    def setUp(self):
        self.command = Command()
        self.manga = Manga.objects.create(name="One Piece",
                                          plot_summary='Twenty two years ago, the legendary pirate, Gold Roger was executed. His final words told')
        self.tags = self.command.get_bs4_soup()
        self.parsed_name, self.des = self.command.parse_manga_information(
            self.tags)

    def test_api_response_parse(self):
        '''test case that determines whether lxml parsing returned non-empty response'''
        self.assertTrue(self.tags)

    def test_manga_name_parsed(self):
        '''test case that determines whether manga name is parsed correctly'''
        self.assertEqual(self.parsed_name, self.manga.name)

    def test_manga_description_parsed(self):
        '''test case that determines whether manga description is parsed correctly'''
        # normalize incoming descriptions
        norm_des = self.des.lower().replace(' ', '')
        norm_sum = self.manga.plot_summary.lower().replace(' ', '')
        self.assertIn(norm_sum, norm_des)


class EpiosdeTests(TestCase):
    def setUp(self):
        self.episode = Episode.objects.create(
            title='Awesome Sample One Piece',
            number=4,
            air_date=dateformat.format(timezone.now(), 'Y-m-d'),
            is_canon=True,
            arc='The Sample Arc'
        )

    def test_episode_content(self):
        self.assertEqual(self.episode.title, 'Awesome Sample One Piece')
        self.assertEqual(self.episode.number, 4)
        self.assertEqual(self.episode.arc, 'The Sample Arc')

    def test_episode_str_repr(self):
        curr_date = dateformat.format(timezone.now(), 'Y-m-d')
        self.assertEqual(
            str(
                self.episode), f"Episode: 4 - Awesome Sample One Piece - Released: {curr_date}"
        )

    def test_home_page_status_code(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)

    def test_home_page_uses_correct_template(self):
        response = self.client.get(reverse("homepage"))
        self.assertTemplateUsed(response, "homepage.html")

    def test_homepage_list_contents(self):
        response = self.client.get(reverse("homepage"))
        self.assertContains(response, "Awesome Sample One Piece")
