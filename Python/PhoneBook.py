# PhoneBook

def display_menu():
    print("\nPhoneBook Menu")
    print("1.add a new contact")
    print("2.Search for a contact")
    print("3.Update contact's phone number")
    print("4.Delet a contact")
    print("5.List of all contacts")
    print("6.Exit")
# display_menu()

def add_contact(PhoneBook):
    name=input("Enter the contact Name:")
    if name in PhoneBook:
        print(f"{name} already exists!!! in your phonebook with number { PhoneBook[name]}")

    else:
        phone=input("Enter your number")
        PhoneBook[name]=phone
        print(f"contact {name} added successfully!!")


def search_contact(PhoneBook):
    name=input("Enter name tobe search")

    if name in PhoneBook:
        print(f"{name} phone number is{PhoneBook[name]}")
    else:
        print(f"{name} not found in the phonebook")


def Update_contact(PhoneBook):
    name=input("Enter your contact u want to Update:")

    if name in PhoneBook:
        new_phone=input(f"Enter new phone number for {name}")
        PhoneBook[name]=new_phone
        print(f"{name}'s phone number is updated successfully!!")

    else:
        print(f"{name} not found in ur phonebook!!")



def Delet_contact(PhoneBook):
    name=input("Enter the name to be delete")
    if name in PhoneBook:
        del PhoneBook[name]
        print(f"contact {name}has been deleted sucessfully!!")
    else:
        print(f"contact {name} not found in ur pb")



def list_contact(PhoneBook):
    if not PhoneBook:
        print("The phonebook is empt.")

    else:
        print("\nphonebook contact:")
        for name,phone in PhoneBook.items():
            print(f"Name :{name}, phone:{phone}")


def main():
    PhoneBook={}
    while(True):
        display_menu()
        choice=input("Enter your choice")

        if choice == "1":
            add_contact(PhoneBook)

        elif choice == "2":
            search_contact(PhoneBook)

        elif choice == "3":
            Update_contact(PhoneBook)

        elif choice == "4":
            Delet_contact(PhoneBook)

        elif choice == "5":
            list_contact(PhoneBook)

        elif choice == "6":
            print("Existing the Phonebook . Goodbyee!")
            break
        else:
            print("Abbe rukk doh")
 
main()