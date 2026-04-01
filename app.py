contact_book = {}

def add_contact():
    new_contact = {}
    name = input("Name: ")
    phone = input("Phone Number: ")
    address = input("Address: ")

    new_contact["Name"] = name
    new_contact["Phone"] = phone
    new_contact["Address"] = address

    contact_book[new_contact["Name"]] = new_contact

def view_all():
    for contacts in contact_book.values():
        for contact_key, contact_value in contacts.items():
            print(contact_key +": " + contact_value)
        print("=" * 20)


def display_options():
    while True:
        user_selection = input("Select action (add | search | delete | all | exit) : ").lower()

        if user_selection == "add":
            add_contact()
        elif user_selection == "search":
            pass
        elif user_selection == "delete":
            pass
        elif user_selection == "all":
            view_all()
        elif user_selection == "exit":
            print("See you soon!")
            break
        else:
            print("Please Enter a valid choice.")


display_options()

