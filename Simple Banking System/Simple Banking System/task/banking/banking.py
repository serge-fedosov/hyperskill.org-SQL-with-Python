from random import randint
import sqlite3

cursor = None
conn = None

msg_menu = """1. Create an account
2. Log into account
0. Exit"""

msg_logged_menu = """\n1. Balance
2. Add income
3. Do transfer
4. Close account
5. Log out
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
msg_account_closed = "The account has been closed!"
msg_enter_income = "Enter income:"
msg_income_added = "Income was added!"
msg_transfer = """Transfer
Enter card number:"""
msg_how_much_transfer = "Enter how much money you want to transfer:"
msg_wrong_card_number = "Probably you made a mistake in the card number. Please try again!"
msg_card_not_exist = "Such a card does not exist."
msg_not_enough_money = "Not enough money!"
msg_success_transfer = "Success!"


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
    global conn
    global cursor

    card = Card()
    print(msg_card.format(card.number, card.pin))

    new_card = (card.number, card.pin, 0)
    cursor.execute("INSERT INTO card(number, pin, balance) VALUES (?, ?, ?);", new_card)
    conn.commit()


def show_balance(card_number):
    global conn
    global cursor

    card = (card_number, )
    cursor.execute("SELECT balance FROM card WHERE number = ?;", card)
    balance = cursor.fetchone()
    print(msg_balance.format(balance[0]))


def log_out_account():
    print(msg_logged_out)


def close_account(card_number):
    global conn
    global cursor

    card = (card_number, )
    cursor.execute("DELETE FROM card WHERE number = ?;", card)
    conn.commit()
    print(msg_account_closed)


def add_income(card_number):
    global conn
    global cursor

    print(msg_enter_income)
    amount = int(input())
    card = (amount, card_number)
    cursor.execute("UPDATE card SET balance = balance + ? WHERE number = ?;", card)
    conn.commit()
    print(msg_income_added)


def check_card_number(card_number_to):
    number = card_number_to[0:len(card_number_to) - 1]
    sum_ = 0
    for i in range(len(number)):
        v = int(number[i])
        if i % 2 == 0:
            v = v * 2
            v = v - 9 if v > 9 else v

        sum_ += v

    last_digit = 10 - sum_ % 10
    last_digit = 0 if last_digit == 10 else last_digit
    return True if last_digit == int(card_number_to[-1]) else False


def do_transfer(card_number):
    global conn
    global cursor

    print(msg_transfer)
    card_number_to = input()
    if not check_card_number(card_number_to):
        print(msg_wrong_card_number)
        return

    card_to = (card_number_to, )
    cursor.execute("SELECT count(*) FROM card WHERE number = ?;", card_to)
    count = cursor.fetchone()
    if count[0] == 0:
        print(msg_card_not_exist)
        return

    print(msg_how_much_transfer)
    amount = int(input())

    card = (card_number, )
    cursor.execute("SELECT balance FROM card WHERE number = ?;", card)
    balance = cursor.fetchone()

    if balance is None or balance[0] < amount:
        print(msg_not_enough_money)
        return

    card = (amount, card_number)
    cursor.execute("UPDATE card SET balance = balance - ? WHERE number = ?;", card)
    conn.commit()
    card_to = (amount, card_number_to)
    cursor.execute("UPDATE card SET balance = balance + ? WHERE number = ?;", card_to)
    conn.commit()
    print(msg_success_transfer)


def log_into_account():
    global conn
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
            add_income(card_number)
        elif command == 3:
            do_transfer(card_number)
        elif command == 4:
            close_account(card_number)
            break
        elif command == 5:
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

    # for pass tests
    cursor.execute("""DELETE FROM card;""")
    conn.commit()


def close_db():
    global conn
    global cursor

    cursor.close()
    conn.close()


connect_db()
menu()
close_db()
