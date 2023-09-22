import Data
import cashier

class SandwichMaker:
    def __init__(self, machine_resources):
        self.machine_resources = machine_resources

    def check_resources(self, ingredients):
        """Returns True when the order can be made, False if ingredients are insufficient."""
        for resource, amount in ingredients.items():
            if resource in self.machine_resources and self.machine_resources[resource] < amount:
                print(f"Sorry, there is not enough {resource}.")
                return False
        return True

    def make_sandwich(self, sandwich_size, order_ingredients, cashier_instance):
        if self.check_resources(order_ingredients):
            cost = Data.recipes[sandwich_size]["cost"]
            print(f"Please insert coins. ")
            coins = cashier_instance.process_coins()  # Use the cashier_instance
            if cashier_instance.transaction_result(coins, cost):  # Use the cashier_instance
                for item, amount in order_ingredients.items():
                    self.machine_resources[item] -= amount
                print(f"{sandwich_size} sandwich is ready. Bon appétit!")

