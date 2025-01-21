from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

# Create objects of classes
coffee_maker = CoffeeMaker()
menu = Menu()
money_machine = MoneyMachine()

# Variable for checking if the machine is on.
is_on = True

while is_on:
    choice = input("What would you like? (espresso/latte/cappuccino): ")
    if choice == "off":
        is_on = False
    elif choice == "report":

        # Print the report with ingredients and money
        coffee_maker.report()
        money_machine.report()
    else:
        # Get the right coffee
        drink = menu.find_drink(choice)

        # Check if resources are sufficient
        if coffee_maker.is_resource_sufficient(drink):

            # Check the price for the coffee
            payment = money_machine.make_payment(drink.cost)

            # Check if there are enough coins
            if payment:

                menu_item = MenuItem(drink.name, drink.ingredients['water'], drink.ingredients['milk'], drink.ingredients['coffee'], drink.cost)

                # Make the coffee
                coffee_maker.make_coffee(menu_item)

