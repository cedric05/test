import sys
import unittest

from challange.prices import APPLE, CHAI, MILK, COFFIE, OATMEAL, ZERO
from challange import *
from unittest import TestCase
import logging


class EdgeCases(TestCase):
    SAMPLE = [APPLE]

    def test_non_negative(self):
        self.assertGreaterEqual(get_total_price(EdgeCases.SAMPLE), 0, "should always be greater than 0")

    def test_not_greater(self):
        self.assertGreaterEqual(get_total_price(EdgeCases.SAMPLE), get_final_price(EdgeCases.SAMPLE))


class ExampleTests(TestCase):

    def test0(self):
        items = [
            CHAI, APPLE
        ]
        self.assertEqual(get_final_price(items), 9.11)

    def test1(self):
        items = [
            CHAI, APPLE, APPLE, APPLE, MILK
        ]
        self.assertEqual(get_final_price(items), 16.61)

    def test2(self):
        items = [
            CHAI, APPLE, COFFIE, MILK
        ]
        self.assertEqual(get_final_price(items), 20.34)

    def test3(self):
        items = [
            MILK, APPLE
        ]
        self.assertEqual(get_final_price(items), 10.75)

    def test4(self):
        items = [
            COFFIE, COFFIE
        ]
        self.assertEqual(get_final_price(items), 11.23)

    def test4(self):
        items = [
            APPLE, APPLE, CHAI, APPLE
        ]
        self.assertEqual(get_final_price(items), 16.61)

    def test_oat(self):
        self.assertAlmostEqual(get_final_price([OATMEAL, APPLE]), OATMEAL.price + APPLE.price / 2)
        self.assertAlmostEqual(get_final_price([OATMEAL, APPLE, APPLE]), OATMEAL.price + APPLE.price * 3 / 2)

    def test_apples(self):
        items = [
            APPLE, APPLE, APPLE, APPLE
        ]
        self.assertEqual(get_final_price(items[:2]), APPLE.price * 2)
        self.assertEqual(get_final_price(items[:3]), 4.50 * 3)
        self.assertEqual(get_final_price(items), 4.50 * 4)

    def test_chai_milk(self):
        self.assertAlmostEqual(get_final_price([CHAI]), CHAI.price)
        self.assertAlmostEqual(get_final_price([MILK]), MILK.price)
        self.assertAlmostEqual(get_final_price([CHAI, MILK]), CHAI.price)
        self.assertAlmostEqual(get_final_price([CHAI, MILK, MILK]), CHAI.price + MILK.price)
        self.assertAlmostEqual(get_final_price([CHAI, MILK, MILK, CHAI]), CHAI.price * 2 + MILK.price)

    def test_BOGO(self):
        self.assertAlmostEqual(get_final_price([COFFIE]), COFFIE.price)
        self.assertAlmostEqual(get_final_price([COFFIE] * 2), COFFIE.price)
        self.assertAlmostEqual(get_final_price([COFFIE] * 3), COFFIE.price * 2)
        self.assertAlmostEqual(get_final_price([COFFIE] * 4), COFFIE.price * 2)

    def test_comb(self):
        self.assertAlmostEqual(get_final_price([COFFIE] * 4 + [CHAI, MILK, MILK]),
                               COFFIE.price * 2 + CHAI.price + MILK.price)
        self.assertAlmostEqual(get_final_price([COFFIE] * 4 + [APPLE] * 1), COFFIE.price * 2 + APPLE.price)
        self.assertAlmostEqual(get_final_price([COFFIE] * 4 + [APPLE] * 2),
                               COFFIE.price * 2 + APPLE.price + APPLE.price)
        self.assertAlmostEqual(get_final_price([COFFIE] * 4 + [APPLE] * 3), COFFIE.price * 2 + 4.5 * 3)


if __name__ == '__main__':
    logging.basicConfig(stream=sys.stderr)
    logging.root.setLevel(logging.DEBUG)
    unittest.main()
