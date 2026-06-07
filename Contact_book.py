contacts = {}

while True:
    print("\n===== Contact Book =====")
    print("1. Add Contact")
    print("2. View Contacts")
    print("3. Search Contact")
    print("4. Delete Contact")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        name = input("Enter Name: ")
        phone = input("Enter Phone Number: ")
        email = input("Enter Email: ")

        contacts[name] = {
            "phone": phone,
            "email": email
        }

        print("Contact Added Successfully!")

    elif choice == "2":
        if not contacts:
            print("No contacts found!")
        else:
            print("\n===== Contact List =====")
            for name, details in contacts.items():
                print(f"Name  : {name}")
                print(f"Phone : {details['phone']}")
                print(f"Email : {details['email']}")
                print("-" * 25)

    elif choice == "3":
        name = input("Enter Name to Search: ")

        if name in contacts:
            print(f"Phone : {contacts[name]['phone']}")
            print(f"Email : {contacts[name]['email']}")
        else:
            print("Contact Not Found!")

    elif choice == "4":
        name = input("Enter Name to Delete: ")

        if name in contacts:
            del contacts[name]
            print("Contact Deleted Successfully!")
        else:
            print("Contact Not Found!")

    elif choice == "5":
        print("Thank You for Using Contact Book!")
        break

    else:
        print("Invalid Choice! Please Try Again.")