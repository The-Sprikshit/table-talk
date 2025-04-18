 #
import pymysql

def initialize_db(host='localhost', user='root', password='', db='Sql_Project'):
    conn = pymysql.connect(host=host, user=user, password=password, db=db)
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Allnames (
            name VARCHAR(255) NOT NULL,
            purpose TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()
    print("Database initialized and table created if it didn't exist.")


def add_to_Allnames(host='localhost', user='root', password='', db='Sql_Project'):
    name = input("Enter the site's name: ").strip()
    purpose = input("Enter the purpose/details: ").strip()
    conn = pymysql.connect(host=host, user=user, password=password, db=db)
    cursor = conn.cursor()
    cursor.execute('INSERT INTO Allnames (name, purpose) VALUES (%s, %s)', (name, purpose))
    conn.commit()
    conn.close()
    print(f"Added {name} with details: {purpose}")


def search_Allnames(host='localhost', user='root', password='', db='NewData'):
    key_or_purpose = input(
        "Want to search the site's name 'name' or its purpose 'purpose'? (type 'exit' to quit): ").strip().lower()
    if key_or_purpose not in ['name', 'purpose']:
        print("Invalid input. Please enter 'name' or 'purpose'.")
        return

    keyword = input(f"Enter a keyword to search within {key_or_purpose}: ").strip()
    conn = pymysql.connect(host=host, user=user, password=password, db=db)
    cursor = conn.cursor()
    query = f"SELECT name, purpose FROM Allnames WHERE {key_or_purpose} LIKE %s"
    cursor.execute(query, ('%' + keyword + '%',))
    results = cursor.fetchall()
    conn.close()

    if results:
        for name, info in results:
            print(f"\nName: {name}")
            print(f"Details: {info}")
    else:
        print(f"No entries found with '{keyword}' in {key_or_purpose}.")


def view_all_names(host='localhost', user='root', password='', db='Sql_Project'):
    conn = pymysql.connect(host=host, user=user, password=password, db=db)
    cursor = conn.cursor()
    cursor.execute('SELECT name FROM Allnames')
    results = cursor.fetchall()
    conn.close()

    if results:
        print("All site names:")
        for (name,) in results:
            print(name)
    else:
        print("No site names found.")


def update_or_delete_Allnames(host='localhost', user='root', password='', db='Sql_Project'):
    name = input("Enter the site's name you want to update or delete: ").strip()

    action = input(
        "Would you like to update the site's data or delete name and all its data? (type 'update' or 'delete'): ").strip().lower()
    if action == 'update':
        update_action = input(
            "Would you like to update the site's name, purpose, or both? (type 'name', 'purpose', or 'both'): ").strip().lower()
        if update_action == 'name':
            new_name = input("Enter the new site's name: ").strip()
            conn = pymysql.connect(host=host, user=user, password=password, db=db)
            cursor = conn.cursor()
            cursor.execute('UPDATE Allnames SET name = %s WHERE name = %s', (new_name, name))
            conn.commit()
            conn.close()
            print(f"Updated site's name from {name} to {new_name}")
        elif update_action == 'purpose':
            new_purpose = input("Enter the new purpose/details: ").strip()
            conn = pymysql.connect(host=host, user=user, password=password, db=db)
            cursor = conn.cursor()
            cursor.execute('UPDATE Allnames SET purpose = %s WHERE name = %s', (new_purpose, name))
            conn.commit()
            conn.close()
            print(f"Updated {name} with new details: {new_purpose}")
        elif update_action == 'both':
            new_name = input("Enter the new site's name: ").strip()
            new_purpose = input("Enter the new purpose/details: ").strip()
            conn = pymysql.connect(host=host, user=user, password=password, db=db)
            cursor = conn.cursor()
            cursor.execute('UPDATE Allnames SET name = %s, purpose = %s WHERE name = %s', (new_name, new_purpose, name))
            conn.commit()
            conn.close()
            print(f"Updated site's name from {name} to {new_name} and purpose to {new_purpose}")
        else:
            print("Invalid input. Please enter 'name', 'purpose', or 'both'.")
    elif action == 'delete':
        conn = pymysql.connect(host=host, user=user, password=password, db=db)
        cursor = conn.cursor()
        cursor.execute('DELETE FROM Allnames WHERE name = %s', (name,))
        conn.commit()
        conn.close()
        print(f"Deleted site with name: {name}")
    else:
        print("Invalid input. Please enter 'update' or 'delete'.")
#
#
def main():
    host = 'localhost'
    user = 'root'
    password = ''
    db = 'Sql_Project'

    initialize_db(host, user, password, db)
    while True:
        action = input(
            "Would you like to enter data, search, update/delete, view all names, or exit? (type 'enter', 'search', 'update/delete', 'view', or 'exit' to quit): ").strip().lower()
        if action == 'exit':
            print("Exiting the program...")
            break
        if action not in ['enter', 'search', 'update','delete', 'view']:
            print("Invalid input. Please enter 'enter', 'search', 'update/delete', 'view', or 'exit'.")
            continue

        if action == 'enter':
            add_to_Allnames(host, user, password, db)
        elif action == 'search':
            search_Allnames(host, user, password, db)
        elif action == 'update' or action=='delete':
            update_or_delete_Allnames(host, user, password, db)
        elif action == 'view':
            view_all_names(host, user, password, db)


main()

