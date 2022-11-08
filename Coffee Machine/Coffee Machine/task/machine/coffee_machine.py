has_water = 400
has_milk = 540
has_coffee_beans = 120
has_cups = 9
has_money = 550
coffee = [[250,   0, 16, 4],
          [350,  75, 20, 7],
          [200, 100, 12, 6]]


def remaining():
    print(f"""
The coffee machine has:
{has_water} ml of water
{has_milk} ml of milk
{has_coffee_beans} g of coffee beans
{has_cups} disposable cups
${has_money} of money""")


def buy():
    global has_water
    global has_milk
    global has_coffee_beans
    global has_cups
    global has_money

    print()
    print("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu:")
    command = input()
    if command == "back":
        return

    coffee_type = int(command) - 1
    if has_water < coffee[coffee_type][0]:
        print("Sorry, not enough water!")
        return

    if has_milk < coffee[coffee_type][1]:
        print("Sorry, not enough milk!")
        return

    if has_coffee_beans < coffee[coffee_type][2]:
        print("Sorry, not enough coffee beans!")
        return

    if has_cups < 1:
        print("Sorry, not enough cups!")
        return

    has_water -= coffee[coffee_type][0]
    has_milk -= coffee[coffee_type][1]
    has_coffee_beans -= coffee[coffee_type][2]
    has_cups -= 1
    has_money += coffee[coffee_type][3]
    print("I have enough resources, making you a coffee!")


def fill():
    global has_water
    global has_milk
    global has_coffee_beans
    global has_cups
    global has_money

    print()
    print("Write how many ml of water you want to add:")
    has_water += int(input())
    print("Write how many ml of milk you want to add:")
    has_milk += int(input())
    print("Write how many grams of coffee beans you want to add:")
    has_coffee_beans += int(input())
    print("Write how many disposable cups you want to add:")
    has_cups += int(input())


def take():
    global has_money

    print(f"I gave you ${has_money}")
    has_money = 0


def menu():
    while True:
        print("Write action (buy, fill, take, remaining, exit): ")
        command = input()
        if command == "buy":
            buy()
        elif command == "fill":
            fill()
        elif command == "take":
            take()
        elif command == "remaining":
            remaining()
        elif command == "exit":
            break

        print()


menu()
