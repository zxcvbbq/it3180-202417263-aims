import unittest

from aims.cart import Cart
from aims.dvd import DigitalVideoDisc


class DiscountTest(unittest.TestCase):
    def test_discounted_total(self):
        cart = Cart()
        cart.items = [DigitalVideoDisc("A", cost=100)]
        for percent, total in [(0, 100), (20, 80), (100, 0)]:
            with self.subTest(percent=percent):
                self.assertAlmostEqual(cart.total_cost_with_discount(percent), total)

    def test_invalid_discount(self):
        cart = Cart()
        for percent in [-1, 150]:
            with self.subTest(percent=percent):
                with self.assertRaises(ValueError):
                    cart.total_cost_with_discount(percent)
