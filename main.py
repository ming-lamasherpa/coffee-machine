from utils import  get_resource_report, is_resources_sufficient, process_coin, add_resources, get_coffee_cost, is_transaction_successful, get_change, serve_coffee, add_money_in_machine,resource_deduction

is_machine_on = True

while is_machine_on:
    choice = input("What would you like?(cappuccino/espresso/latte) : ")

    if choice.lower() == 'off':
        is_machine_on = False

    elif choice.lower() == 'report':
        get_resource_report()

    elif choice.lower() == 'add resource':
        add_resources()

    else:
        if choice not in ["cappuccino", "espresso", "latte"] :
            print(f"Sorry {choice} is not available. Please select from the menu.")
        
        else :
           if is_resources_sufficient(choice):
              paid = process_coin(choice)
              cost = get_coffee_cost(choice)

              if is_transaction_successful(paid,cost):
                  get_change(paid,cost)
                  serve_coffee(choice)
                  add_money_in_machine(cost)
                  resource_deduction(choice)

              else:
                  print(f"Sorry not enough money for {choice}. Money refunded.")