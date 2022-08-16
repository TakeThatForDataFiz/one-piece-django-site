from django.test import TestCase
from django.utils import timezone, dateformat
from .models import Episode
from django.urls.base import reverse

# Create your tests here.


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
