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
    "money": 0.00,
}

turn_machine_off = False

while not turn_machine_off:

    # TODO 3. Print report: when user enters "report" to the prompt. Shows current resources
    def print_report():
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: £{resources['money']}")


    def check_resources(drink):
        if resources["water"] >= MENU[drink]["ingredients"]["water"]:
            pass
            if resources["milk"] >= MENU[drink]["ingredients"]["milk"]:
                pass
                if resources["coffee"] >= MENU[drink]["ingredients"]["coffee"]:
                    return True
        else:
            print("Sorry, there are not enough resources.")
            return False


    def process_coins():
        print("Please insert coins.")
        pennies = int(input("How many pennies?")) * 0.01
        nickles = int(input("How many nickles?")) * 0.05
        dimes = int(input("How many dimes?")) * 0.10
        quarters = int(input("How many quarters?")) * 0.25
        resources["money"] = pennies + nickles + dimes + quarters


    def is_transaction_successful(drink):
        if MENU[drink]["cost"] == resources["money"]:
            return True
        elif MENU[drink]["cost"] > resources["money"]:
            print("Sorry that's not enough money. Money refunded")
            resources["money"] = 0.00
            return False
        elif MENU[drink]["cost"] < resources["money"]:
            change = resources["money"] - MENU[drink]["cost"]
            resources["money"] - change
            change = round(change, 2)
            print(f"Here is £{change} in change.")
            return True


    # TODO 1. Prompt user by asking "What would you like? (expresso/latte/cappuccino)
    user_input = input("What would you like? (expresso/latte/cappuccino)?")
    # TODO 2. Turn off the Coffee Machine by entering "off" to the prompt.
    if user_input == "off":
        turn_machine_off = True
    if user_input == "report":
        print_report()

    # TODO 4. Check resources sufficient. When user picks a drink,
    #  the program should check if there enough resources.
    resources_check = check_resources(user_input)
    # TODO 5. Process Coins. If there are sufficient resources, prompt user to insert coins.
    if resources_check:
        process_coins()
    # TODO 6: Check transactions successful: check if user has inserted enough money.
    check_transactions = is_transaction_successful(user_input)
    if check_transactions:
        water = resources["water"] - MENU[user_input]["ingredients"]["water"]
        milk = resources["milk"] - MENU[user_input]["ingredients"]["milk"]
        coffee = resources["coffee"] - MENU[user_input]["ingredients"]["coffee"]
        print(f"Here is your {user_input}. Enjoy!")

    # TODO 7: Make Cofffee: ingredients to make drink should be deducted from coffee machine resources.
