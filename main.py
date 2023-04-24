# Makes 3 Hot Flavours: Expresso, Latte, Cappuccino
# Expresso: £1.50, 50ml Water, 18g Coffee
# Latte: £2.50, 200ml Water, 24g Coffe, 150ml Milk
# Cappuccino: £3.00, 250ml Water, 24g Coffee, 100ml Milk
#
# Starting resources in the coffee machine:
# 300ml Water
# 200ml Milk
# 100g of Coffee
#
# Coin Operated Machine
# Penny = 0.01
# Nickel = 0.05
# Dime = 0.10
# Quarter = 0.25
#
# Program Requirements:
#
# Print Report: machine should be able to tell us what resources it has left
# Check resources sufficient: look through resources, check it against the recipe and report findings
# Process coins: calculate how much money coins inserted are worth and change
# Check transaction successful:
# Make the coffee: deduct the resources used to make the coffee.
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
}

# TODO 1. Prompt user by asking "What would you like? (expresso/latte/cappuccino)
# TODO 2. Turn off the Coffee Machine by entering "off" to the prompt.
# TODO 3. Print report: when user enters "report" to the prompt. Shows current resources
# TODO 4. Check resources sufficient. When user picks a drink, the program should check if there enough resources.
# TODO 5. Process Coins. If there are sufficient resources, prompt user to insert coins.
# TODO 6: Check transactions successful: check if user has inserted enough money.
# TODO 7: Make Cofffee: ingredients to make drink should be deducted from coffee machine resources.
