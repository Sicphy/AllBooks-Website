from django.test import TestCase
from genres.models import Genre
from goods.models import Good

# Create your tests here.

class GenreClassTest(TestCase):
    
    def create_genre(self, name="Adventure"):
        return Genre.objects.create(name=name)

    def test_genre_creation(self):
        g = self.create_genre()
        self.assertTrue(isinstance(g, Genre))

    
