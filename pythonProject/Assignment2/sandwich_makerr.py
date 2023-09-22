import Data
class SandwichMaker:
    def __init__(self, resources):
        self.machine_resources = resources

    def check_resources(self, ingredients):
        """Returns True when order can be made, False if ingredients are insufficient."""
        # checks to see if there are enough resources to make the sandwich
        # if there isn't enough, it'll say sorry there isnt enough
        for resource, amount in ingredients.items():
            if resource in self.machine_resources and self.machine_resources[resource] < amount:
                print(f"Sorry there is not enough {resource}.")
                return False
        return True

    def make_sandwich(self, sandwich_size, order_ingredients):
        """Deduct the required ingredients from the resources.
           Hint: no output"""
        if self.check_resources(order_ingredients):
            cost = main.recipes[sandwich_size]["cost"]
            print(f"Please insert coins. ")
            coins = self.process_coins()
            if self.transaction_result(coins, cost):
                for item, amount in order_ingredients.items():
                    self.machine_resources[item] -= amount
                print(f"{sandwich_size} sandwich is ready. Bon appetit!")