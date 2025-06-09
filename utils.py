from resources_db import machine_resources as resources
from resources_db import COFFEE_MENU

def get_resources_report():
    print(f"Water: {resources.get('water', ' ')}ml")
    print(f"Milk: {resources.get('milk', ' ')}ml")
    print(f"Coffee: {resources.get('coffee', ' ')}gm")
    print(f"Money: ${resources.get('money', 0):.2f}")

def is_resource_sufficient(choice):
    is_resource_suff = True
    for ingred, qty in COFFEE_MENU[choice]["ingredients"].items():
        if resources.get(ingred, 0) < qty:
            print(f"Sorry, there is not enough {ingred}!")
            is_resource_suff =  False
            break
    return is_resource_suff

def process_coins(choice):
    print("Please Insert coins:")
    quarters = int(input("How many quarters?: "))   # $0.25
    dimes = int(input("How many Dimes?: "))      # $0.10
    nickels = int(input("How many Nickels?: "))    # $0.05
    pennies = int(input("How many Pennies?: "))    # $0.01
    total = quarters * 0.25 + dimes * 0.10 + nickels * 0.05 + pennies * 0.01
    cost = COFFEE_MENU.get(choice,{}).get("money", " ")

    if total > cost:
        print(f"here is ${round(total - cost, 2)} in charge.🪙")
        print(f"Here is your {choice}🍵.Enjoy!")
    else:
        print("Sorry that's not money.Money refunded.")