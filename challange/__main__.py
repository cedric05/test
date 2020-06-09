import sys
from sys import argv

from challange import STORE, get_final_price
from pprint import pprint
if __name__ == "__main__":
    cart = argv[1:]
    if len(cart) == 0:
        print("usage python -m challange item1 item2 item3")
        sys.exit(1)
    items = []
    for name in cart:
        try:
            items.append(STORE.get_item(name))
        except:
            print(f"item `{name}` not listed in database, please correct and run")
            sys.exit(1)
    print(f"total price calculated for {items} is {get_final_price(items)}$")
