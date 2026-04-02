import json
contact_book = {}

def load_data():
    with open("data.json", "r") as f:
        data = json.load(f)
        return(data)

def save_data():
    with open("data.json", "w") as f:
        json.dump(contact_book, f)


def add_contact():
    new_contact = {}
    name = input("Name: ")
    phone = input("Phone Number: ")
    address = input("Address: ")

    new_contact["Name"] = name
    new_contact["Phone"] = phone
    new_contact["Address"] = address

    contact_book[new_contact["Name"]] = new_contact
    save_data()

def view_all():
    if contact_book.values():
        for contacts in contact_book.values():
            for contact_key, contact_value in contacts.items():
                print(contact_key +": " + contact_value)
            print("=" * 20)
    else:
        print("There are no contacts to view.")
        print("=" * 20)

def find_contact():
    contact = input("Contact Name: ")
    if contact in contact_book:
        for contact_key, contact_value in contact_book[contact].items():
            print(contact_key + ": " + contact_value)
        print("=" * 20)
    else:
        print("Contact was not found.")

def remove_contact():
    contact = input("Name: ")
    if contact in contact_book:
        contact_book.pop(contact)
        print(f"{contact} was removed.")
    else:
        print("Contact was not found.")
        save_data()

def display_options():
    saved_data = load_data()
    contact_book.update(saved_data)
            
    while True:
        user_selection = input("Select action (add | search | delete | all | exit) : ").lower()

        if user_selection == "add":
            add_contact()
        elif user_selection == "search":
            find_contact()
        elif user_selection == "delete":
            remove_contact()
        elif user_selection == "all":
            view_all()
        elif user_selection == "exit":
            print("See you soon!")
            break
        else:
            print("Please Enter a valid choice.")


display_options()
