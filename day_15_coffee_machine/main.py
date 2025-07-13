from dictionaries import MENU, resources

# MENU = dict{
#     MENU[coffee]: dict{
#         MENU[coffee][ingredients]:dict{
#             MENU[coffee][ingredients][water]: ml
#             MENU[coffee][ingredients][milk]: ml
#             MENU[coffee][ingredients][coffee]: g
#         }
#         MENU[coffee][cost]: int
#     }
# }

bank = 0

def report(res):
    print("\nThe amount of resources remaining in the coffee machine in milliliters and grams")
    for item in res:
        print(f"> {item.capitalize()}: {res[item]}")
    print(f"> Money: ${bank}")

def is_resource_sufficient(order_ingredients):
    """Returns True when order can be made, False if ingredients are insufficient."""
    for ingredient in order_ingredients:
        if order_ingredients[ingredient] > resources[ingredient]:
            print(f"Sorry there is not enough {ingredient}.")
            return False
    return True


def coin_counting():
    """Returns the total calculated from coins inserted."""
    print("Please insert coins.")
    total = int(input("how many quarters?: ")) * 0.25
    total += int(input("how many dimes?: ")) * 0.1
    total += int(input("how many nickles?: ")) * 0.05
    total += int(input("how many pennies?: ")) * 0.01
    return total

def is_transaction_successful(money_received, drink_cost):
    """Return True when the payment is accepted, or False if money is insufficient."""
    if money_received < drink_cost:
        print("Sorry that's not enough money. Money refunded.")
        return False
    else:
        change = round(money_received - drink_cost, 2)
        print(f"Here is ${change} in change.")
        global bank
        bank += drink_cost
        return True

def make_coffee(drink_name, order_ingredients):
    """Deduct the required ingredients from the resources."""
    for ingredients in order_ingredients:
        resources[ingredients] -= order_ingredients[ingredients]
    print(f"Here is your {drink_name} ☕️. Enjoy!")


is_on = True

while is_on:
    choice = input("What would you like? (espresso/latte/cappuccino): ").lower()
    if choice == "off":
        print("Coffee machine is off. Bye!")
        is_on = False
    elif choice == "report":
        report(resources)
    else:
        if choice == "espresso" or choice == "latte" or choice == "cappuccino":
            drink = MENU[choice]
            if is_resource_sufficient(drink["ingredients"]):
                payment = coin_counting()
                if is_transaction_successful(payment, drink["cost"]):
                    make_coffee(choice, drink["ingredients"])
        else:
            print("\nSorry, but we don't have this type of coffee.\nPlease choose from the three provided.\n")

