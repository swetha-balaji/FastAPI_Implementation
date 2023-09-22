import Data
import cashier
import sandwich_makerr
from sandwich_makerr import SandwichMaker
from cashier import Cashier

# Make an instance of other classes here
resources = Data.resources
recipes = Data.recipes
sandwich_maker_instance = SandwichMaker(resources)
cashier_instance = Cashier()

def main():
    while True:
        # Prompting user about what they'd like
        user_input = input("What would you like? (small/medium/large/off/report): ").lower()
        # 'off' turns off the machine, 'report' shows remaining resources

        if user_input == "off":
            break
        elif user_input == "report":
            for item, amount in sandwich_maker_instance.machine_resources.items():
                print(f"{item.capitalize()}: {amount} {'slice(s)' if item == 'bread' else 'ounce(s)' if item == 'cheese' else 'slice(s)'}")
        elif user_input in recipes:
            sandwich_size = user_input
            order_ingredients = recipes[sandwich_size]["ingredients"]
            if sandwich_maker_instance.check_resources(order_ingredients):
                sandwich_maker_instance.make_sandwich(sandwich_size, order_ingredients)
        else:
            print("Invalid input. Please select a valid option: small, medium, large, off, or report.")

if __name__ == "__main__":
    main()
