from random import randint
import sqlite3

cursor = None
conn = None

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

    def __init__(self):
        Card.customer_account_number += 1
        self.number = Card.IIN + f"{Card.customer_account_number:09}"
        self.generate_checksum()
        self.pin = f"{randint(0, 9999):04}"
        self.balance = 0

    def generate_checksum(self):
        sum_ = 0
        number = self.number
        for i in range(len(number)):
            v = int(number[i])
            if i % 2 == 0:
                v = v * 2
                v = v - 9 if v > 9 else v

            sum_ += v

        last_digit = 10 - sum_ % 10
        last_digit = 0 if last_digit == 10 else last_digit
        self.number += str(last_digit)


def create_account():
    global cursor

    card = Card()
    print(msg_card.format(card.number, card.pin))

    new_card = (card.number, card.pin, 0)
    cursor.execute("INSERT INTO card(number, pin, balance) VALUES (?, ?, ?)", new_card)
    conn.commit()


def show_balance(card_number):
    find_card = (card_number, )
    cursor.execute("SELECT balance FROM card WHERE number = ?;", find_card)
    balance = cursor.fetchone()
    print(msg_balance.format(balance[0]))


def log_out_account():
    print(msg_logged_out)


def log_into_account():
    global cursor

    print(msg_enter_card_number)
    card_number = input()
    print(msg_enter_card_pin)
    card_pin = input()

    find_card = (card_number, card_pin)
    cursor.execute("SELECT count(*) FROM card WHERE number = ? AND pin = ?;", find_card)
    count = cursor.fetchone()
    if count[0] == 1:
        print(msg_logged_in)
    else:
        print(msg_wrong_card)
        return

    while True:
        print(msg_logged_menu)
        command = int(input())
        if command == 1:
            show_balance(card_number)
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
       

def connect_db():
    global conn
    global cursor

    conn = sqlite3.connect('card.s3db')
    cursor = conn.cursor()

    cursor.execute("""CREATE TABLE IF NOT EXISTS card(
        id INTEGER PRIMARY KEY,
        number TEXT,
        pin TEXT,
        balance INTEGER DEFAULT 0
        );""")

    conn.commit()


def close_db():
    global conn
    global cursor

    cursor.close()
    conn.close()


connect_db()
menu()
close_db()
