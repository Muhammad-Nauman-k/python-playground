from Menu_file import Menu
from Maker_file import Maker
from Money_machine_file import MoneyMachine

#------------- Making Objects ----------
menu = Menu()
maker = Maker()
money_machine = MoneyMachine()

is_on = True

while is_on:
    choice = input(f"What do you want {menu.get_menu_items()}:      ").lower()
    
    if choice == "off":  # If the owner wants to close the machine
        is_on = False
    elif choice == "report": # Owner wants to know the total Resources & Money
        maker.report()
        money_machine.total_money()
    else:
        cost = maker.cost_of_item(choice) # Cost of the item chossen
        print(f"Please insert {cost}$ for your {choice}")
        if maker.is_resource_sufficent(choice) and money_machine.make_payment(cost):  # Check if resources are avaliable & Make Payment if(True & True) then make coffee
            maker.make_coffee(choice)
    