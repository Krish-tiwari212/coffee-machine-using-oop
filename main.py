from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine
coffee_make = CoffeeMaker()
money_mac = MoneyMachine()
coffee_make.report()
money_mac.report()
men=Menu()
a=0
while a == 0:
    user_input = input(f"What do you want {men.get_items()}? : ").lower()
    if user_input == "off":
        a = 1
    elif user_input == "report":
        coffee_make.report()
        money_mac.report()
    else:
        a=men.find_drink(user_input)
        c = coffee_make.is_resource_sufficient(a)
        if c is True:
            money_mac.make_payment(a.cost)
            coffee_make.make_coffee(a)
            a=0
        elif c is False:
            a=0