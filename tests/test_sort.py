import unittest

from aims.cart import Cart
from aims.dvd import DigitalVideoDisc


class SortTest(unittest.TestCase):
    def test_sort_by_title(self):
        cart = Cart()
        b = DigitalVideoDisc("B", cost=10)
        a = DigitalVideoDisc("A", cost=2)
        cart.items = [b, a]
        cart.sort_by_title()
        self.assertEqual(cart.items, [a, b])
        self.assertEqual(cart.total_cost(), 12)

    def test_sort_by_cost(self):
        cart = Cart()
        expensive = DigitalVideoDisc("A", cost=10)
        cheap = DigitalVideoDisc("B", cost=2)
        cart.items = [expensive, cheap]
        cart.sort_by_cost()
        self.assertEqual(cart.items, [cheap, expensive])
        self.assertEqual(cart.total_cost(), 12)
