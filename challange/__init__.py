import logging
from typing import List

from .discounts import DISCOUNTS_HANDLERS
from .prices import ItemStore, Item

STORE = ItemStore()
logger = logging.getLogger("main")


def get_final_price(items: List[Item]) -> float:
    """

    :type items: returns total price after deducting price
    """
    total = get_total_price(items)
    discount: float = get_total_price_down(items)
    final_price = total - discount
    assert final_price >= 0.0, "final price should be greater than zero"
    logger.debug(f"total price before discount {total} discount is {discount} , final price is {final_price}")
    return round(final_price, 2)


def get_total_price(items):
    total: float = sum(ItemStore.get_price(item) for item in items)
    return total


def get_total_price_down(items: List[Item]) -> float:
    total_price_down = 0
    for handler, enabled in DISCOUNTS_HANDLERS.items():
        if enabled:
            price_down = handler.get_discount(items)
            logger.debug(
                f"ran discount with handler {handler.code} for items f{items} and price down is f{price_down}")
            total_price_down += price_down
    return total_price_down
