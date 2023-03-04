from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
coffeemaker = CoffeeMaker()
moneymachine = MoneyMachine()
while True:
    type = input("What would you like? (" + menu.get_items() + "): ")
    if type == "off":
        break
    elif type == 'report':
        coffeemaker.report()
        moneymachine.report()
    elif menu.find_drink(type) is not None:
        menuItem = menu.find_drink(type)
        if coffeemaker.is_resource_sufficient(menuItem):
            if moneymachine.make_payment(menuItem.cost):
                coffeemaker.make_coffee(menuItem)




