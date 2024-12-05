# Simple contacts system
contacts = {}

def add_contact(name, phone):
    contacts[name] = phone
    print(f"Contact '{name}' added.")

def view_contacts():
    if contacts:
        print("Contacts List:")
        for name, phone in contacts.items():
            print(f"Name: {name}, Phone: {phone}")
    else:
        print("No contacts found.")

def delete_contact(name):
    if name in contacts:
        del contacts[name]
        print(f"Contact '{name}' deleted.")
    else:
        print(f"Contact '{name}' not found.")

# Main loop
while True:
    print(" ---Contact list--- ")
    print("\n1. Add Contact")
    print("2. View Contacts")
    print("3. Delete Contact")
    print("4. Exit")
    
    
    choice = input("choose an option (1-4): ")

    if choice == '1':
        name = input("Enter name: ")
        phone = input("Enter phone number: ")
        add_contact(name, phone)
    elif choice == '2':
        view_contacts()
    elif choice == '3':
        name = input("Enter name of the contact to delete: ")
        delete_contact(name)
    elif choice == '4':
        print("Exiting the system.")
        break
    else:
        print("Invalid choice, please try again.")
   