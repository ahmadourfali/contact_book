contact_book = {}

for _ in range(3):
    
    new_contact = {}
    name = input("Name: ")
    phone = input("Phone Number: ")
    address = input("Address: ")

    new_contact["name"] = name
    new_contact["phone"] = phone
    new_contact["address"] = address

    contact_book[new_contact["name"]] = new_contact

print(contact_book)
