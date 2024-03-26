from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

is_play = True

menum = Menu()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()

while is_play:
    choice = input(f"What would you like ?({menum.get_items()})")
    if choice == "report":
        coffee_maker.report()
        money_machine.report()
    elif choice == "off":
        print("The machine is closing...")
    else:
        drink=menum.find_drink(choice)
        if coffee_maker.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost):
            coffee_maker.make_coffee(drink)

