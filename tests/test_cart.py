import unittest
from contextlib import redirect_stdout
from io import StringIO

from aims.cart import Cart
from aims.dvd import DigitalVideoDisc


class CartTest(unittest.TestCase):
    def test_add_dvd_until_full(self):
        cart = Cart()
        with redirect_stdout(StringIO()):
            for index in range(20):
                self.assertTrue(cart.add_dvd(DigitalVideoDisc(str(index))))
            self.assertFalse(cart.add_dvd(DigitalVideoDisc("DVD 21")))
        self.assertEqual(len(cart.items), 20)

    def test_total_cost(self):
        cart = Cart()
        self.assertEqual(cart.total_cost(), 0)
        cart.items = [DigitalVideoDisc("A", cost=19.95),
                      DigitalVideoDisc("B", cost=24.95),
                      DigitalVideoDisc("C", cost=18.99)]
        self.assertAlmostEqual(cart.total_cost(), 63.89)
