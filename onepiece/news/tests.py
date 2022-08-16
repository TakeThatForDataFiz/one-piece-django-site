from django.test import TestCase
from django.utils import timezone, dateformat
from .models import Episode

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
