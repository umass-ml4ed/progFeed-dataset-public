# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

class VendingMachine:
    def __init__(self):
        self.items = {}
        self.balance = 0.0
        self.total_sales = 0.0
        self.sales_history = []

    def add_item(self, name, price, quantity):
        if name in self.items:
            self.items[name]["qty"] += quantity
            self.items[name]["price"] = price
        else:
            self.items[name] = {"price": price, "qty": quantity}
        print(f"{quantity} {name}(s) added to inventory")

    def get_item_price(self, name):
        if name not in self.items:
            print("Invalid item")
            return None
        return self.items[name]["price"]

    def get_item_quantity(self, name):
        if name not in self.items:
            print("Invalid item")
            return None
        return self.items[name]["qty"]

    def list_items(self):
        if not self.items:
            print("No items in the vending machine")
            return
        print("Available items:")
        for name in sorted(self.items.keys()):
            price = self.items[name]["price"]
            qty = self.items[name]["qty"]
            print(f"{name} (${price}): {qty} available")

    def insert_money(self, amount):
        if amount not in [1.0, 2.0, 5.0]:
            print("Invalid amount")
            return
        self.balance = round(self.balance + amount, 2)
        print(f"Balance: {self.balance}")

    def purchase(self, name):
        if name not in self.items:
            print("Invalid item")
            return
        price = self.items[name]["price"]
        qty = self.items[name]["qty"]
        if qty == 0:
            print(f"Sorry {name} is out of stock")
            return
        if self.balance < price:
            print(f"Insufficient balance. Price of {name} is {price}")
            return
        self.items[name]["qty"] -= 1
        self.balance = round(self.balance - price, 2)
        self.total_sales = round(self.total_sales + price, 2)
        self.sales_history.append((name, price))
        print(f"Purchased {name}")
        print(f"Balance: {self.balance}")

    def output_change(self):
        if self.balance == 0:
            print("No change")
        else:
            print(f"Change: {self.balance}")
            self.balance = 0.0

    def remove_item(self, name):
        if name not in self.items:
            print("Invalid item")
            return
        del self.items[name]
        print(f"{name} removed from inventory")

    def empty_inventory(self):
        self.items = {}
        print("Inventory cleared")

    def get_total_sales(self):
        return self.total_sales

    def stats(self, N):
        if not self.sales_history:
            print("No sale history in the vending machine")
            return
        recent_sales = self.sales_history[-N:]
        num_records = len(recent_sales)
        print(f"Sale history for the most recent {num_records} purchase(s):")
        stats = {}
        for item, price in recent_sales:
            if item not in stats:
                stats[item] = {"qty": 0, "sales": 0.0}
            stats[item]["qty"] += 1
            stats[item]["sales"] += price
        for name in sorted(stats.keys()):
            total = stats[name]["sales"]
            qty = stats[name]["qty"]
            print(f"{name}: ${total} for {qty} purchase(s)")