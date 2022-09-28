from enum import Enum
import sqlite3
from helper import Remove_contacts, Search_contacts, addcontact, get_contacts
conn = sqlite3.connect("my_contacts.db")
cur = conn.cursor()
# cur.execute("CREATE TABLE Contacts(Contacts_id INTEGER PRIMARY KEY, Name char(30), Cell char(35));")


class MyMenu(Enum):
    ADD = 2
    PRINT = 3
    DELETE = 4
    SEARCH = 5
    EXIT = 6


# display menu, get user selection
def menu():
    for opt in MyMenu:
        print(f"{opt.value} - {opt.name}")

    user_selection = input("your selection:")
    return int(user_selection)


def main():
    user_selection = menu()  # get user selection from menu
    while user_selection != MyMenu.EXIT.value:
        if user_selection == MyMenu.ADD.value:
            addcontact()  # add new contact to contacts
        if user_selection == MyMenu.PRINT.value:
            get_contacts()  # print all contacts
        if user_selection == MyMenu.DELETE.value:
            Remove_contacts()  # delete a contact
        if user_selection == MyMenu.SEARCH.value:
            Search_contacts()
        user_selection = menu()
        conn.close()


if __name__ == "__main__":
    main()
