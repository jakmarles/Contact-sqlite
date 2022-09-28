import sqlite3
conn = sqlite3.connect("my_contacts.db")
cur = conn.cursor()


def addcontact():
    s_name = input('Name:')
    s_cell = input('Cell:')
    cur.execute("""
    INSERT INTO Contacts(Name, Cell)
    VALUES (?,?)
    """, (s_name, s_cell))
    conn.commit()
    print('Contact entered successfully.')


def get_contacts():
    with conn:
        cur.execute("SELECT * FROM Contacts WHERE Name IS NOT NULL")
        print('Contacts:')
        print(cur.fetchall())


def Search_contacts():
    with conn:
        sql = '''SELECT * FROM Contacts WHERE Name = ?'''
        searchinput = input("Name to search: ")
        result = []
        cur.execute(sql, (searchinput,))
        result.append(cur.fetchall())
        if result == [[]]:
            print("Cant find a contact with that name.")
        else:
            print("Contact found.")
            print(result)


def Remove_contacts():
    with conn:
        get_contacts()
        sql = '''SELECT * FROM Contacts WHERE Contacts_id = ?'''
        searchinput = input("Contacts id to remove: ")
        result = []
        cur.execute(sql, (searchinput,))
        result.append(cur.fetchall())
        if result == [[]]:
            print("Cant find a contact with that name.")
        else:
            sql_delete_query = '''Update Contacts set name = NULL,Cell = NULL WHERE Contacts_id = ?'''
            result = []
            cur.execute(sql_delete_query, (searchinput,))
            result.append(cur.fetchall())
            print('Contact has beeen removed')
