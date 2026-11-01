import unittest

from aims.dvd import DigitalVideoDisc
from aims.search import search_by_title


class TitleSearchTest(unittest.TestCase):
    def test_search_ignores_case(self):
        lion = DigitalVideoDisc("The Lion King")
        wars = DigitalVideoDisc("Star Wars")
        for keyword in ["lion", "LION", "LiOn"]:
            with self.subTest(keyword=keyword):
                self.assertEqual(search_by_title([lion, wars], keyword), [lion])
        self.assertEqual(search_by_title([lion, wars], "missing"), [])
        self.assertEqual(search_by_title([], "lion"), [])
