import logging
from itertools import filterfalse
from typing import List

from challange.prices import COFFIE, APPLE, CHAI, MILK, OATMEAL, Item

logger = logging.getLogger("discounts")


class DiscountHandler():
    """ no need of this method, they are not inhertied any way"""

    def _get_discount(self, items: List[Item]) -> float:
        raise NotImplemented("not implemented")

    def get_discount(self, items):
        value = self._get_discount(items)
        assert value >= 0.0, "price down should never be negative"
        return round(value,2)


class BuyOneGetOneCofffe(DiscountHandler):
    """
        Buy-One-Get-One-Free Special on Coffee. (Unlimited)
    """
    code = "BOGO"

    def _get_discount(self, items: List[Item]):
        number = len(tuple(filterfalse(lambda item: not item == COFFIE, items)))
        return (number // 2) * COFFIE.price

    def __str__(self):
        return BuyOneGetOneCofffe.code;


class ThreeApples(DiscountHandler):
    """
         If you buy 3 or more bags of Apples, the price drops to $4.50.
    """
    code = "APPL"

    def _get_discount(self, items: List[Item]):
        number = len(tuple(filterfalse(lambda item: not item == APPLE, items)))
        if number >= 3:
            logger.debug(f"more than three apples found in {items}")
            return number * (APPLE.price - 4.50)
        return 0

    def __str__(self):
        return ThreeApples.APPL;


class BuyChaigetMilk(DiscountHandler):
    """
         Purchase a box of Chai and get milk free. (Limit 1)
    """
    code = "CHMK"

    def _get_discount(self, items: List[Item]):
        chai_ordered = False
        milk_ordered = False
        for item in items:
            if item == MILK and not milk_ordered:
                milk_ordered = True
            if item == CHAI and not chai_ordered:
                chai_ordered = True
            if milk_ordered and chai_ordered:
                return MILK.price
        return 0

    def __str__(self):
        return BuyChaigetMilk.code


class OatMealApple(DiscountHandler):
    """
        Purchase a bag of Oatmeal and get 50% off a bag of Apples
    """
    code = "APOM"

    def _get_discount(self, items: List[Item]):
        apple_ordered = False
        oats_ordered = False
        for item in items:
            if item == OATMEAL and not oats_ordered:
                oats_ordered = True
            if item == APPLE and not apple_ordered:
                apple_ordered = True
            if oats_ordered and apple_ordered:
                return APPLE.price / 2
        return 0

    def __str__(self):
        return OatMealApple.code


DISCOUNTS_HANDLERS = {
    BuyOneGetOneCofffe(): True,
    ThreeApples(): True,
    BuyChaigetMilk(): True,
    OatMealApple(): True
}
