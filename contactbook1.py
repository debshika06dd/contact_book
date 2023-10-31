contacts={}

def add_contact():
        name=input("Contact Name: ")
        number=input("Contact Number: ")
        email_Id=input("Email_ID: ")
        contacts[name]=email_Id
        contacts[name]=number
        print(f"Contact: {name} added successfully.")

def search_contact():
        name=input("Enter the contact to search: ")
        
        if name in contacts:
                print(f"Contact name: {name}, Phone Number: {contacts[name]}, Email_ID: {contacts[name]}")
       
        else:
                print("Sorry! This CONTACT doesn't exist. ")

def list_contact():     
        print("Contacts in the Contact Book: ")
        for name, number in contacts.items:
                print(f"Contact name: {name}, Phone Number: {contacts[name]}, Email_ID: {contacts[name]}")
        
def update_contact():
        name=input("Enter the Contact Name that is to be updated: ")
        
        if name in contacts:
              new_number=input("Enter the new Phone Number: ")
              contacts[name]=new_number
              new_email_ID=input("Enter the new Email ID")
              contacts[name]=new_email_ID
              print(f"Contact {name} updated successfully. ")

def remove_contact():
    name = input("Enter the contact's name to remove: ")
    if name in contacts:
        del contacts[name]
        print(f"Contact {name} removed successfully.")
    else:
        print(f"Contact {name} not found in the Contact Book.")


while True:
    print("\nSelect one of the Contact Book Menu:")
    print("1. Add Contact")
    print("2. Search Contact")
    print("3. List Contacts")
    print("4. Remove Contact")
    print("5. Update Contact")
    print("6. Exit")

    choice = input("Enter your choice (1/2/3/4/5/6): ")

    if choice == "1":
        add_contact()
    elif choice == "2":
        search_contact()
    elif choice == "3":
        list_contact()
    elif choice == "4":
        remove_contact()
    elif choice == "5":
        update_contact()
    elif choice == "6":
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Please enter a valid option (1/2/3/4/5).")
