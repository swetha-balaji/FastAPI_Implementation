class Cashier:

    def process_coins(self):
        """Returns the total calculated from coins inserted.
           Hint: include input() function here, e.g. input("how many quarters?: ")"""
        # if there are enough resources it prompts the user to insert coins for payment
        # user to insert coins for payment
        large_dollar = int(input("how many large dollars?: "))
        half_dollar = int(input("how many half dollars?: "))
        quarter = int(input("how many quarters?: "))
        nickel = int(input("how many nickels?: "))
        total_money = (large_dollar * 1.00 + half_dollar * 0.50 + quarter * 0.25 + nickel * 0.05)
        # large dollar = $1
        # half dollar = $0.50
        # quarter = $0.25
        # nickel = $0.05
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