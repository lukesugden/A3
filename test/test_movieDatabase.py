import os
from unittest import TestCase
from rottenonions.movie import MovieDatabase


class TestMovieDatabase(TestCase):
    def test_get(self):
        md = MovieDatabase(database_path=os.path.abspath('../resources/Data1000Movies.csv'))
        m = md.get('Prometheus', 2012)
        if m.title != 'Prometheus' or m.year != 2012:
            self.fail()
