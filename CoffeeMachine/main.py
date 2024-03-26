MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "milk": 0,
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

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

coins=0
is_flag=True
coffee={}
while is_flag:
    secim=input("What would you like? (espresso/latte/cappuccino): ")

    if secim == "report":
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Coins: ${coins}")
    elif secim == "off":
        print("The machine is shutting down...")
        is_flag=False
    else:
        coffee=MENU[secim]
        if coffee["ingredients"]["water"]>resources["water"]:
            print("Sorry there is not enough water.")
            continue
        elif coffee["ingredients"]["milk"]>resources["milk"]:
            print("Sorry there is not enough milk.")
            continue
        elif coffee["ingredients"]["coffee"]>resources["coffee"]:
            print("Sorry there is not enough coffee.")
            continue
        else:
            print("Everything is enough")
            resources["water"] -= coffee["ingredients"]["water"]
            resources["milk"] -= coffee["ingredients"]["milk"]
            resources["coffee"] -= coffee["ingredients"]["coffee"]

        A = float(input("How many quarters will you throw: "))
        B = float(input("How many dimes will you throw: "))
        C = float(input("How many nickles will you throw: "))
        D = float(input("How many pennies will you throw: "))
        SUM=(A*0.25)+(B*0.1)+(C*0.05)+(D*0.01)
        if SUM<coffee["cost"]:
            print("Sorry that's not enough money. Money refunded.")
            continue
        elif SUM>coffee["cost"]:
            coins += coffee["cost"]
            kalan=SUM-coffee["cost"]
            print(f"Here is ${kalan:.2f} dollars in change.")
        else:
            coins += coffee["cost"]
        print(f"Here is your {secim} Enjoy !")