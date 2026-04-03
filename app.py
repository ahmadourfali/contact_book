import json

def load_data():
    try:
        with open("data.json", "r") as f:
            return json.load(f)
    except FileNotFoundError:
        print("File was not found.")
        return {}

def save_data(contact_book):
    with open("data.json", "w") as f:
        json.dump(contact_book, f)

def validate_input(prompt):
    while True:
        user_input = input(prompt)
        if user_input.replace(" ", "").isalnum() and len(user_input) < 20:
            return user_input
        else:
            print("enter a valid name or address <Not more than 20 letters and numbers> ")
            continue


def add_contact(contact_book):
    new_contact = {}
    name = validate_input("Name: ")
    phone = validate_input("Phone Number: ")
    address = validate_input("Address: ")

    new_contact["Name"] = name.upper()
    new_contact["Phone"] = phone
    new_contact["Address"] = address

    contact_book[new_contact["Name"]] = new_contact
    save_data(contact_book)

def view_all(contact_book):
    if not contact_book:
        print("There are no contacts to view.")
        return # Exit the function early

    for contact in contact_book.values():
        for key, value in contact.items():
            print(f"{key}: {value}")
        print("=" * 20)

def find_contact(contact_book):
    contact = input("Contact Name: ").upper()
    print("=" * 20)
    if contact in contact_book:
        for contact_key, contact_value in contact_book[contact].items():
            print(contact_key + ": " + contact_value)
        print("=" * 20)
    else:
        print("Contact was not found.")

def remove_contact(contact_book):
    contact = input("Name: ").upper()
    if contact in contact_book:
        contact_book.pop(contact)
        print(f"{contact} was removed.")
    else:
        print("Contact was not found.")
    save_data(contact_book)

def display_options(contact_book):
    while True:
        print("=" * 60)
        user_selection = input("Select action (add | search | delete | all | exit) : ").lower()
        print("=" * 60)

        if user_selection == "add":
            add_contact(contact_book)
        elif user_selection == "search":
            find_contact(contact_book)
        elif user_selection == "delete":
            remove_contact(contact_book)
        elif user_selection == "all":
            view_all(contact_book)
        elif user_selection == "exit":
            print("See you soon!")
            break
        else:
            print("Please Enter a valid choice.")


if __name__ == "__main__":
    contact_book = load_data()
    display_options(contact_book)
