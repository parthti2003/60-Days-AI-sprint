contacts = {}  # Dictionary to store contacts

def add_contact():
    name = input("Enter contact name: ").strip()
    phone = input("Enter phone number: ").strip()
    contacts[name] = phone
    print(f"Contact '{name}' added successfully!\n")

def view_contacts():
    if not contacts:
        print("No contacts found.\n")
    else:
        print("\n--- Contact List ---")
        for name, phone in contacts.items():
            print(f"{name}: {phone}")
        print()

def search_contact():
    name = input("Enter name to search: ").strip()
    if name in contacts:
        print(f"{name}'s number is {contacts[name]}\n")
    else:
        print("Contact not found.\n")

def delete_contact():
    name = input("Enter name to delete: ").strip()
    if name in contacts:
        del contacts[name]
        print(f"Contact '{name}' deleted successfully!\n")
    else:
        print("Contact not found.\n")

def contact_book():
    while True:
        print("----- Contact Book -----")
        print("1. Add Contact")
        print("2. View All Contacts")
        print("3. Search Contact")
        print("4. Delete Contact")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ").strip()

        if choice == '1':
            add_contact()
        elif choice == '2':
            view_contacts()
        elif choice == '3':
            search_contact()
        elif choice == '4':
            delete_contact()
        elif choice == '5':
            print("Exiting Contact Book. Goodbye!")
            break
        else:
            print("Invalid choice! Please enter a number between 1 and 5.\n")

# Run the Contact Book
contact_book()
