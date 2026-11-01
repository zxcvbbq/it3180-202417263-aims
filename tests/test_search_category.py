import unittest

from aims.dvd import DigitalVideoDisc
from aims import search


class CategorySearchTest(unittest.TestCase):
    def test_search_by_category(self):
        lion = DigitalVideoDisc("The Lion King", "Animation")
        wars = DigitalVideoDisc("Star Wars", "Science Fiction")
        aladdin = DigitalVideoDisc("Aladdin", "Animation")
        self.assertTrue(callable(getattr(search, "search_by_category", None)))
        self.assertEqual(search.search_by_category([lion, wars, aladdin], "Animation"),
                         [lion, aladdin])
        self.assertEqual(search.search_by_category([lion, wars], "Drama"), [])
