from menu import MENU, resources

water = resources["water"]
milk = resources["milk"]
coffee = resources["coffee"]
money = 0

# TODO:function for report


def report():
    print(f"water:{water}g\nmilk:{milk}g\ncoffe:{coffee}g\nmoney:${money}\n")


def process_coins():
    print("Insert coins")
    quarters = int(input("quarters:")) * 0.25
    dimes = int(input("dimes:")) * 0.10
    nickles = int(input("nickles:")) * 0.05
    pennies = int(input("Pennies:")) * 0.01
    money_given = (quarters + dimes + nickles + pennies)
    return round(money_given, 2)


def transaction_successful(given):
    if given < MENU[order]["cost"]:
        print(f"Sorry that's not enough money, money refunded:${money_gotten}")
    elif given > MENU[order]["cost"]:
        change = money_gotten - MENU[order]["cost"]
        print(f"Here's your coffe ☕, your change:${change}, enjoy!😊")
    else:
        print("Here's your coffe ☕, enjoy!😊")


task = "on"
while task == "on":
    order = input("What would you like? espresso,latte,cappuccino?:").lower()
    if order == "report":
        report()
    elif order == "off":
        task = "off"
    elif order == "espresso":
        if MENU["espresso"]["ingredients"]["water"] > water:
            print("insufficient water, please refill.")
        elif MENU["espresso"]["ingredients"]["coffee"] > coffee:
            print("insufficient milk, please refill.")
        else:
            water -= MENU["espresso"]["ingredients"]["water"]
            coffee -= MENU["espresso"]["ingredients"]["coffee"]
            money += MENU[order]["cost"]
            money_gotten = process_coins()
            transaction_successful(money_gotten)


    elif order == "cappuccino" or order == "latte":
        if MENU[order]["ingredients"]["water"] > water:
            print("insufficient water, please refill.")
        elif MENU[order]["ingredients"]["coffee"] > coffee:
            print("insufficient coffe, please refill.")
        elif MENU[order]["ingredients"]["milk"] > milk:
            print("insufficient milk, please refill.")
        else:
            water -= MENU[order]["ingredients"]["water"]
            milk -= MENU[order]["ingredients"]["milk"]
            coffee -= MENU[order]["ingredients"]["coffee"]
            money += MENU[order]["cost"]
            money_gotten = process_coins()
            transaction_successful(money_gotten)
    else:
        print("Unknown entry")
