from data import MENU, resources
# Import MENU and resources from the data module

from prettytable import PrettyTable
# Import PrettyTable to display the report in a tabular format

# Initialize a PrettyTable object
table = PrettyTable()

# Flag to control the main loop
work = False
# Variable to track the profit
profit = 0

def resource_check():
    # Function to check if there are enough resources to make the desired drink

    if order == "e":
        # Check for espresso
        if (resources['water'] >= MENU['espresso']['ingredients']['water'] and
                resources['coffee'] >= MENU['espresso']['ingredients']['coffee']):
            # If there are enough resources, proceed to money transaction
            money()
        else:
            # If resources are insufficient, print appropriate messages
            if resources['water'] < MENU['espresso']['ingredients']['water']:
                print("Sorry! there is not enough water.")
            if resources['coffee'] < MENU['espresso']['ingredients']['coffee']:
                print("sorry! there is not enough coffee.")

    elif order == "l":
        # Check for latte
        if (resources['water'] >= MENU['latte']['ingredients']['water'] and
                resources['milk'] >= MENU['latte']['ingredients']['milk'] and
                resources['coffee'] >= MENU['latte']['ingredients']['coffee']):
            # If there are enough resources, proceed to money transaction
            money()
        else:
            # If resources are insufficient, print appropriate messages
            if resources['water'] < MENU['latte']['ingredients']['water']:
                print("Sorry! there is not enough water.")
            if resources['milk'] < MENU['latte']['ingredients']['milk']:
                print("Sorry! there is not enough milk.")
            if resources['coffee'] < MENU['latte']['ingredients']['coffee']:
                print("sorry! there is not enough coffee.")

    elif order == "c":
        # Check for cappuccino
        if (resources['water'] >= MENU['cappuccino']['ingredients']['water'] and
                resources['milk'] >= MENU['cappuccino']['ingredients']['milk'] and
                resources['coffee'] >= MENU['cappuccino']['ingredients']['coffee']):
            # If there are enough resources, proceed to money transaction
            money()
        else:
            # If resources are insufficient, print appropriate messages
            if resources['water'] < MENU['cappuccino']['ingredients']['water']:
                print("Sorry! there is not enough water.")
            if resources['milk'] < MENU['cappuccino']['ingredients']['milk']:
                print("Sorry! there is not enough milk.")
            if resources['coffee'] < MENU['cappuccino']['ingredients']['coffee']:
                print("sorry! there is not enough coffee.")

def money():
    # Function to handle the money transaction and update resources and profit

    global resources, profit
    # Declare resources and profit as global to modify them within this function

    print("Please insert money into the machine (coins only): ")
    # Prompt user to insert money

    # Collect money inputs from the user
    quarters = int(input("insert all the quarters: "))
    dimes = int(input("insert all the dimes: "))
    nickels = int(input("insert all the nickels: "))
    pennies = int(input("insert all the pennies: "))
    # Calculate the total money inserted
    total = (quarters * 0.25) + (dimes * 0.10) + (nickels * 0.05) + (pennies * 0.01)

    if order == "e" and total >= MENU['espresso']['cost']:
        # Check if the order is espresso and if the total money is sufficient
        print("Here is your espresso. ☕ Enjoy!")
        if total > MENU['espresso']['cost']:
            # If more money was inserted than required, provide change
            print(f"and here is your ${round(total-MENU['espresso']['cost'],2)} change.")
        # Deduct the ingredients from resources
        resources['water'] -= MENU['espresso']['ingredients']['water']
        resources['coffee'] -= MENU['espresso']['ingredients']['coffee']
        # Add the cost to the profit
        profit += MENU['espresso']['cost']

    elif order == "l" and total >= MENU['latte']['cost']:
        # Check if the order is latte and if the total money is sufficient
        print("Here is your latte. ☕ Enjoy!")
        if total > MENU['latte']['cost']:
            # If more money was inserted than required, provide change
            print(f"and here is your ${round(total-MENU['latte']['cost'],2)} change.")
        # Deduct the ingredients from resources
        resources['water'] -= MENU['latte']['ingredients']['water']
        resources['milk'] -= MENU['latte']['ingredients']['milk']
        resources['coffee'] -= MENU['latte']['ingredients']['coffee']
        # Add the cost to the profit
        profit += MENU['latte']['cost']

    elif order == "c" and total >= MENU['cappuccino']['cost']:
        # Check if the order is cappuccino and if the total money is sufficient
        print("Here is your cappuccino. ☕ Enjoy!")
        if total > MENU['cappuccino']['cost']:
            # If more money was inserted than required, provide change
            print(f"and here is your ${round(total-MENU['cappuccino']['cost'],2)} change.")
        # Deduct the ingredients from resources
        resources['water'] -= MENU['cappuccino']['ingredients']['water']
        resources['milk'] -= MENU['cappuccino']['ingredients']['milk']
        resources['coffee'] -= MENU['cappuccino']['ingredients']['coffee']
        # Add the cost to the profit
        profit += MENU['cappuccino']['cost']

    else:
        # If not enough money was inserted, refund the money
        print("Sorry that's not enough money. Money refunded")

while not work:
    # Main loop to keep the coffee machine running

    if (resources['milk'] >= MENU['cappuccino']['ingredients']['milk'] or
            resources['water'] >= MENU['espresso']['ingredients']['water'] or
            resources['coffee'] >= MENU['espresso']['ingredients']['coffee']):
        # Check if there are enough resources to make at least one drink

        # Prompt user to place an order
        order = input("What would you like to have? "
                      "\nwe have espresso($1.5), latte($2.5), cappuccino($3.0)"
                      "\ntype E for espresso, L for latte, and C for cappuccino\n").lower()

        if order == "off":
            # If user types 'off', stop the machine
            work = True
        elif order == "report":
            # If user types 'report', display the current resources and profit
            table.add_column("Ingredients", ["water", "milk", "coffee", "profit"])
            table.add_column("Quantity", [f"{resources['water']}ml", f"{resources['milk']}ml",
                             f"{resources['coffee']}g", f"${profit}"])
            print(table)
        elif order == "e" or order == "l" or order == "c":
            # If user types a valid order, check resources
            resource_check()
        else:
            # If user types an invalid order, notify the user
            print("Sorry Boss! we are not offering that currently. Try something available on our menu.")

    else:
        # If resources are insufficient, stop the machine
        print("insufficient resources for next order.")
        work = True
