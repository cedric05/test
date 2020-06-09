class ItemNotAvailable(Exception):
    message = "item is not available/listed"
    pass


class Item(object):
    def __init__(self, name, price, helpful_name):
        self.name = name
        self.price = price
        self.helpfull_name = helpful_name

    def __eq__(self, other):
        return super.__eq__(self, other)

    def __str__(self):
        return f"{self.helpfull_name} : {self.price}$"

    def __repr__(self):
        return self.__str__()

    def __add__(self, other):
        if isinstance(other, Item):
            return self.price + other.price
        super.__add__(self, other)  # ideally we should throw, we are letting super class to handle it in its own way


ZERO = Item("ZERO", 0.0, "NONE")
CHAI = Item("CH1", 3.11, "CHAI")
APPLE = Item("AP1", 6.00, "APPLE")
COFFIE = Item("CF1", 11.23, "COFFIE")
MILK = Item("MK1", 4.75, "MILK")
OATMEAL = Item("OM1", 4.69, "OATMEAL")


class ItemStore():
    _PRICES = [
        CHAI, APPLE, COFFIE, MILK, OATMEAL
    ]

    @staticmethod
    def get_price(item: Item):
        assert item.price >= 0, "price should not be less than zero"
        return item.price

    @staticmethod
    def get_item(name) -> Item:
        for price in ItemStore._PRICES:
            if price.name == name:
                return price
        raise ItemNotAvailable(f"item {name} not listed")
