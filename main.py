from resources_db import machine_resources as resources
def get_resources_report():
    print(f"Water: {resources.get('water',' ')}ml")
    print(f"milk: {resources.get('milk',' ')}ml")
    print(f"coffee: {resources.get('coffee',' ' )}gm")
    print(f"money: {resources.get('money',' ')}")
is_machine_on =True

while is_machine_on:
    choice = input("what would you lke? (espresso/latte/cappuccino):")
    if choice.lower() == "off":
        is_machine_on = False
   
    elif choice.lower() == "report":
        get_resources_report()