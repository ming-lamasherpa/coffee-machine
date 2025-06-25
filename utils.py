from resources import machine_resources, Coffee_Menu


def get_resource_report():
    print(f"Water = {machine_resources.get('water','')}ml")
    print(f"Milk = {machine_resources.get('milk','')}ml")
    print(f"Coffee = {machine_resources.get('coffee','')}gm")
    print(f"Money = ${machine_resources.get('money','')}")

def is_resources_sufficient(choice):
    is_sufficient = True
    for ingred,qty in  get_ingredients(choice):
        if machine_resources.get(ingred, 0) < qty:
            print(f"Sorry, there is not enough {ingred}")
            is_sufficient = False
            break
    return is_sufficient

def process_coin(choice):
    print(f'Please insert coins:')
    quarters = int(input(f"How many quarters? "))
    dimes = int(input(f"How many dimes? "))
    nickles = int(input(f"How many nickles? "))
    pennies = int(input(f"How many pennies? "))
    total = quarters * 0.25 + dimes * 0.10 + nickles * 0.05 + pennies * 0.01
    return total


def get_coffee_cost(choice):
    cost = Coffee_Menu.get(choice,{}).get('money','')
    return cost

def is_transaction_successful(paid,cost):
    return False if paid < cost else True


   
def get_change(paid,cost):
        print(f"Here is your ${round(paid-cost,2)} change.")


def get_ingredients(choice):
     return Coffee_Menu.get(choice,{}).get("ingredients",{}).items()
def serve_coffee(choice):
        print(f"Here is your {choice}!!Enjoy!!")


def add_money_in_machine(cost):
    if isinstance(cost, (int,float)):
            machine_resources['money'] += cost
    

def resource_deduction(choice):
    for ingred,qty in get_ingredients(choice):
            machine_resources[ingred] -= qty




def add_resources():
    water = int(input("How much water (ml) to add? "))
    milk = int(input("How much milk (ml) to add? "))
    coffee = int(input("How much coffee (gm) to add? "))

    machine_resources['water'] += water
    machine_resources['milk'] += milk
    machine_resources['coffee'] += coffee

    print("Resources added  successfully!!")