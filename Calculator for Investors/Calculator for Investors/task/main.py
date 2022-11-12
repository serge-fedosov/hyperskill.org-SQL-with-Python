MSG_MAIN_MENU = """
MAIN MENU
0 Exit
1 CRUD operations
2 Show top ten companies by criteria
"""

MSG_CRUD_MENU = """
CRUD MENU
0 Back
1 Create a company
2 Read a company
3 Update a company
4 Delete a company
5 List all companies
"""

MSG_TOP_TEN_MENU = """
TOP TEN MENU
0 Back
1 List by ND/EBITDA
2 List by ROE
3 List by ROA
"""

MSG_ENTER_OPTION = "Enter an option:"
MSG_GOODBYE = "Have a nice day!"
MSG_INVALID_OPTION = "Invalid option!"
MSG_NOT_IMPLEMENTED = "Not implemented!"


def crud_menu():
    while True:
        print(MSG_CRUD_MENU)
        print(MSG_ENTER_OPTION)
        command = input()
        if command == "0":
            pass
        elif command == "1":
            pass
        elif command == "2":
            pass
        elif command == "3":
            pass
        elif command == "4":
            pass
        elif command == "5":
            pass
        else:
            print(MSG_INVALID_OPTION)

        break

    print(MSG_NOT_IMPLEMENTED)


def top_ten_menu():
    while True:
        print(MSG_TOP_TEN_MENU)
        print(MSG_ENTER_OPTION)
        command = input()
        if command == "0":
            pass
        elif command == "1":
            pass
        elif command == "2":
            pass
        elif command == "3":
            pass
        else:
            print(MSG_INVALID_OPTION)

        break

    print(MSG_NOT_IMPLEMENTED)


def main_menu():
    while True:
        print(MSG_MAIN_MENU)
        print(MSG_ENTER_OPTION)
        command = input()
        if command == "0":
            break
        elif command == "1":
            crud_menu()
        elif command == "2":
            top_ten_menu()
        else:
            print(MSG_INVALID_OPTION)

    print(MSG_GOODBYE)


main_menu()
