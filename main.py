MENU = {
    "expresso": {
        "ingredients": {
            "water": 50,
            "milk": 0,
            "coffee": 18,
        },
        "cost": 1.50,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.50,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.00,
    },
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
    "money": 0,
}


# TODO 3. Print report: when user enters "report" to the prompt. Shows current resources
def print_report():
    print(f"Water: {resources['water']}ml")
    print(f"Milk: {resources['milk']}ml")
    print(f"Coffee: {resources['coffee']}g")
    print(f"Money: £{resources['money']}")


turn_machine_off = False

while not turn_machine_off:
    # TODO 1. Prompt user by asking "What would you like? (expresso/latte/cappuccino)
    user_input = input("What would you like? (expresso/latte/cappuccino)?")

    # TODO 2. Turn off the Coffee Machine by entering "off" to the prompt.
    if user_input == "off":
        turn_machine_off = True
    if user_input == "report":
        print_report()

# TODO 4. Check resources sufficient. When user picks a drink, the program should check if there enough resources.
# TODO 5. Process Coins. If there are sufficient resources, prompt user to insert coins.
# TODO 6: Check transactions successful: check if user has inserted enough money.
# TODO 7: Make Cofffee: ingredients to make drink should be deducted from coffee machine resources.
