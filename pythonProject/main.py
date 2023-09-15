### Data ###

recipes = {
    "small": {
        "ingredients": {
            "bread": 2,  ## slice
            "ham": 4,  ## slice
            "cheese": 4,  ## ounces
        },
        "cost": 1.75,
    },
    "medium": {
        "ingredients": {
            "bread": 4,  ## slice
            "ham": 6,  ## slice
            "cheese": 8,  ## ounces
        },
        "cost": 3.25,
    },
    "large": {
        "ingredients": {
            "bread": 6,  ## slice
            "ham": 8,  ## slice
            "cheese": 12,  ## ounces
        },
        "cost": 5.5,
    }
}

resources = {
    "bread": 12,  ## slice
    "ham": 18,  ## slice
    "cheese": 24,  ## ounces
}


### Complete functions ####

class SandwichMachine:

    def __init__(self, machine_resources):
        """Receives resources as input.
           Hint: bind input variable to self variable"""
        self.machine_resources = machine_resources

    def check_resources(self, ingredients):
        """Returns True when order can be made, False if ingredients are insufficient."""
        #checks to see if there are enough resources to make the sandwich
        #if there isn't enough, it'll say sorry there isnt enough
        for resource, amount in ingredients.items():
            if resource in self.machine_resources and self.machine_resources[resource] < amount:
                print(f"Sorry there is not enough {resource}.")
                return False
        return True

    def process_coins(self):
        """Returns the total calculated from coins inserted.
           Hint: include input() function here, e.g. input("how many quarters?: ")"""
        # if there are enough resources it prompts the user to insert coins for payment
        large_dollar = int(input("how many large dollars?: "))
        half_dollar = int(input("how many half dollars?: "))
        quarter = int(input("how many quarters?: "))
        nickel = int(input("how many nickels?: "))
        total_money = (large_dollar * 1.00 + half_dollar * 0.50 + quarter * 0.25 + nickel * 0.05)
        #large dollar = $1
        #half dollar = $0.50
        #quarter = $0.25
        #nickel = $0.05
        return total_money

    def transaction_result(self, coins, cost):
        """Return True when the payment is accepted, or False if money is insufficient.
           Hint: use the output of process_coins() function for cost input"""
        # basically shows if funds are sufficient or not so we use if statements to make it easier
        if coins >= cost:
            change = coins - cost
            if change > 0:
                print(f"Here is ${change:.2f} in change.")
            return True
        else:
            print("Sorry that's not enough money. Money refunded.")
            return False

    def make_sandwich(self, sandwich_size, order_ingredients):
        """Deduct the required ingredients from the resources.
           Hint: no output"""
        if self.check_resources(order_ingredients):
            cost = recipes[sandwich_size]["cost"]
            print(f"Please insert coins. ")
            coins = self.process_coins()
            if self.transaction_result(coins, cost):
                for item, amount in order_ingredients.items():
                    self.machine_resources[item] -= amount
                print(f"{sandwich_size} sandwich is ready. Bon appetit!")

### Make an instance of SandwichMachine class and write the rest of the codes ###
machine = SandwichMachine(resources)

while True:
    #Prompting user about what they'd like
    user_input = input("What would you like? (small/medium/large/off/report): ").lower()
    #off turns off machine
    #report shows remaining resources

    if user_input == "off":
        break
    elif user_input == "report":
        for item, amount in machine.machine_resources.items():
            print(f"{item.capitalize()}: {amount} {'slice(s)' if item == 'bread' else 'ounce(s)' if item == 'cheese' else 'slice(s)'}")
    elif user_input in recipes:
        sandwich_size = user_input
        order_ingredients = recipes[sandwich_size]["ingredients"]
        if machine.check_resources(order_ingredients):
            machine.make_sandwich(sandwich_size, order_ingredients)
    else:
        print("Invalid input. Please select a valid option: small, medium, large, off, or report.")