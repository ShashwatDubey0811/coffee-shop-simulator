# Coffee Machine Game

print("Welcome to Shashwat's Coffee Shop!! ")

Menu = {
    "Espresso": {
        "ingredients": {
        "water": 50,
        "coffee": 18,
    },
    "cost": 1.5
    },

    "Latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
    },
        "cost": 2.5
    },

    "Capuccinno": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
    },
        "cost": 3.0
    },

    "Cold Coffee": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
    },
        "cost": 4.5
    },

    "Hot Coffee": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
    },
        "cost": 5.5
},
}

profit = 0
resources = {

    "water": 300,
    "milk": 200,
    "coffee": 100
}

def is_resources_sufficient(order_ingredients):
    for items in order_ingredients:
        if order_ingredients[items] >= resources[items]:
            print(f"Sorry there is not enough {items}.")
            return False

    return True

def process_coin():
    """Return the total calculated from coins inserted."""
    print('Please insert a coin.')
    total = int(input('How many quarters?: ')) * 0.25
    total += int(input('How many dimes?: ')) * 0.10
    total += int(input('How many nickles?: ')) * 0.05
    total += int(input('How many pennies?: ')) * 0.01
    return total


def transaction_successful(money_received, drink_cost):
    if money_received >= drink_cost:
        change = round(money_received - drink_cost, 2)
        print(f"Here is ${change} in change. ")
        global profit
        profit += drink_cost
        return True
    else:
        print("Sorry that's not enough money. Money Refunded. " )
        return False
    
def make_coffee(drink_name,order_ingredients):
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Here is your {drink_name}. Enjoy")



switch_on = True

while  switch_on:
    choice = input("What would you Like?: (Espresso/ Latte/ Capuccinno/ Cold Coffee/ Hot Coffee): ")

    if choice == "off":
        switch_on = False

    if choice == "report":
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f" Money: ${profit}")
    else:
        drink = Menu[choice]
        print(drink)
        if is_resources_sufficient(drink["ingredients"]):
            payment = process_coin()
            if transaction_successful(payment, drink["cost"]):
                make_coffee(choice,drink["ingredients"])


