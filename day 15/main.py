MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}
profit = 0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


def is_resources_sufficient(order):
    for item in order:
        if (order[item] > resources[item]):
            print("Sorry there is no enough ", item)
            return False
    return True


def process_coins():
    print("Please insert coins")
    total = 0
    total += int(input("How many Quaters : ")) * 0.25
    total += int(input("How many dimes : ")) * 0.1
    total += int(input("How many nickels : ")) * 0.05
    total += int(input("How many pennies : ")) * 0.01
    return total


def payment_successful(t_amount, d_cost):
    if t_amount >= d_cost:
        change = round((t_amount - d_cost), 2)
        print(f"Here is the change : {change}")
        global profit
        profit += d_cost
        return True
    else:
        print("Sorry that's not an enough amount.Money refunded")
        return False


def make_coffee(drink_name, order_ingridients):
    for item in order_ingridients:
        resources[item] -= order_ingridients[item]
    print(f"Here is your {drink_name}.Enjoy!!")


is_on = True
while is_on:
    choice = input("What would you like? (espresso/latte/cappuccino): ")
    if choice == "off":
        is_on = False
    elif choice == "report":
        print("Water : ", resources["water"])
        print("Milk : ", resources["milk"])
        print("Coffee : ", resources["coffee"])
        print("Profit : ", profit)
    else:
        drink = MENU[choice]
        if is_resources_sufficient(drink["ingredients"]):
            payment = process_coins()
            if payment_successful(payment, drink["cost"]):
                make_coffee(choice, drink["ingredients"])