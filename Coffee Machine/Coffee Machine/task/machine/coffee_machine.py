class CoffeeMachine:
    coffee = [[250,   0, 16, 4],
              [350,  75, 20, 7],
              [200, 100, 12, 6]]

    STATE_READY = 1
    STATE_WAIT_COMMAND = 2
    STATE_WHAT_WANT_BUY = 3
    STATE_FILL_WATER = 4
    STATE_FILL_MILK = 5
    STATE_FILL_COFFEE_BEANS = 6
    STATE_FILL_CUPS = 7

    def __init__(self):
        self.has_water = 400
        self.has_milk = 540
        self.has_coffee_beans = 120
        self.has_cups = 9
        self.has_money = 550
        self.state = CoffeeMachine.STATE_READY

    def remaining(self):
        print(f"""
The coffee machine has:
{self.has_water} ml of water
{self.has_milk} ml of milk
{self.has_coffee_beans} g of coffee beans
{self.has_cups} disposable cups
${self.has_money} of money""")

    def buy(self, command):
        if command == "back":
            return

        coffee_type = int(command) - 1
        if self.has_water < CoffeeMachine.coffee[coffee_type][0]:
            print("Sorry, not enough water!")
            return

        if self.has_milk < CoffeeMachine.coffee[coffee_type][1]:
            print("Sorry, not enough milk!")
            return

        if self.has_coffee_beans < CoffeeMachine.coffee[coffee_type][2]:
            print("Sorry, not enough coffee beans!")
            return

        if self.has_cups < 1:
            print("Sorry, not enough cups!")
            return

        self.has_water -= CoffeeMachine.coffee[coffee_type][0]
        self.has_milk -= CoffeeMachine.coffee[coffee_type][1]
        self.has_coffee_beans -= CoffeeMachine.coffee[coffee_type][2]
        self.has_cups -= 1
        self.has_money += CoffeeMachine.coffee[coffee_type][3]
        print("I have enough resources, making you a coffee!")

    def fill(self, command):
        fill = int(command)
        if self.state == CoffeeMachine.STATE_FILL_WATER:
            self.has_water += fill
            print("Write how many ml of milk you want to add:")
            self.state = CoffeeMachine.STATE_FILL_MILK
        elif self.state == CoffeeMachine.STATE_FILL_MILK:
            self.has_milk += fill
            print("Write how many grams of coffee beans you want to add:")
            self.state = CoffeeMachine.STATE_FILL_COFFEE_BEANS
        elif self.state == CoffeeMachine.STATE_FILL_COFFEE_BEANS:
            self.has_coffee_beans += fill
            print("Write how many disposable cups you want to add:")
            self.state = CoffeeMachine.STATE_FILL_CUPS
        elif self.state == CoffeeMachine.STATE_FILL_CUPS:
            self.has_cups += fill
            self.show_menu()

    def take(self):
        print(f"I gave you ${self.has_money}")
        self.has_money = 0

    def show_menu(self):
        print("Write action (buy, fill, take, remaining, exit): ")
        self.state = CoffeeMachine.STATE_WAIT_COMMAND

    def execute(self, command):
        if self.state == CoffeeMachine.STATE_READY:
            self.show_menu()
        elif self.state == CoffeeMachine.STATE_WAIT_COMMAND:
            if command == "buy":
                print()
                print("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu:")
                self.state = CoffeeMachine.STATE_WHAT_WANT_BUY
            elif command == "fill":
                self.state = CoffeeMachine.STATE_FILL_WATER
                print()
                print("Write how many ml of water you want to add:")
            elif command == "take":
                self.take()
                self.show_menu()
            elif command == "remaining":
                self.remaining()
                self.show_menu()
            elif command == "exit":
                return
        elif self.state == CoffeeMachine.STATE_WHAT_WANT_BUY:
            self.state = CoffeeMachine.STATE_READY
            self.buy(command)
            self.show_menu()
        elif self.state == CoffeeMachine.STATE_FILL_WATER or self.state == CoffeeMachine.STATE_FILL_MILK \
                or self.state == CoffeeMachine.STATE_FILL_COFFEE_BEANS or self.state == CoffeeMachine.STATE_FILL_CUPS:
            self.fill(command)


coffee_machine = CoffeeMachine()
user_command = "start"
while user_command != "exit":
    coffee_machine.execute(user_command)
    user_command = input()

