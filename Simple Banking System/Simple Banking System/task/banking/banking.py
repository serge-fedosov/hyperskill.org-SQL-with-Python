from random import randint

msg_menu = """1. Create an account
2. Log into account
0. Exit"""

msg_logged_menu = """\n1. Balance
2. Log out
0. Exit"""

msg_card = """
Your card has been created
Your card number:
{}
Your card PIN:
{}
"""

msg_enter_card_number = "\nEnter your card number:"
msg_enter_card_pin = "Enter your PIN:"
msg_wrong_card = "\nWrong card number or PIN!"
msg_logged_in = "\nYou have successfully logged in!"
msg_logged_out = "\nYou have successfully logged out!"
msg_balance = "\nBalance: {}"
msg_bye = "\nBye!"


class Card:
    IIN = "400000"
    customer_account_number = 0
    cards = []

    def __init__(self):
        Card.customer_account_number += 1
        self.number = Card.IIN + f"{Card.customer_account_number:09}" + "0"
        self.pin = randint(0, 9999)
        self.balance = 0
        Card.cards.append(self)


def create_account():
    card = Card()
    print(msg_card.format(card.number, card.pin))


def show_balance(card):
    print(msg_balance.format(card.balance))


def log_out_account():
    print(msg_logged_out)


def log_into_account():
    print(msg_enter_card_number)
    card_number = input()
    print(msg_enter_card_pin)
    card_pin = int(input())

    current_card = None
    logged = False
    for card in Card.cards:
        if card.number == card_number and card.pin == card_pin:
            print(msg_logged_in)
            current_card = card
            logged = True

    if not logged:
        print(msg_wrong_card)
        return

    while True:
        print(msg_logged_menu)
        command = int(input())
        if command == 1:
            show_balance(current_card)
        elif command == 2:
            log_out_account()
            break
        elif command == 0:
            return 0


def menu():
    while True:
        print(msg_menu)
        command = int(input())
        if command == 1:
            create_account()
        elif command == 2:
            if log_into_account() == 0:
                print(msg_bye)
                break
        elif command == 0:
            print(msg_bye)
            break
       
            
menu()
