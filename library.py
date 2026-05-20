books = []


# Add Book
def add_book():

    name = input("Enter book name: ")

    found = False

    for b in books:

        if b["name"] == name:
            found = True

    if found == True:

        print("Book already exists")

    else:

        books.append({
            "name": name
        })

        print("Book added successfully")


# View Books
def view_books():

    if len(books) == 0:

        print("No books available")

    else:

        print("------ Book List ------")

        for b in books:

            print("Book Name :", b["name"])

            print("----------------------")


# Delete Book
def delete_book():

    name = input("Enter book name to delete: ")

    found = False

    for b in books:

        if b["name"] == name:

            books.remove(b)

            print("Book deleted successfully")

            found = True

            break

    if found == False:

        print("Book not found")


# Issue Book
def issue_book():

    name = input("Enter book name to issue: ")

    found = False

    for b in books:

        if b["name"] == name:

            books.remove(b)

            print("Book issued successfully")

            found = True

            break

    if found == False:

        print("Book not available")


# Return Book
def return_book():

    name = input("Enter book name to return: ")

    books.append({
        "name": name
    })

    print("Book returned successfully")


# Main Menu
while True:

    print("===== LIBRARY MANAGEMENT SYSTEM =====")

    print("1. Add Book")
    print("2. View Books")
    print("3. Delete Book")
    print("4. Issue Book")
    print("5. Return Book")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":

        add_book()

    elif choice == "2":

        view_books()

    elif choice == "3":

        delete_book()

    elif choice == "4":

        issue_book()

    elif choice == "5":

        return_book()

    elif choice == "6":

        print("Program Exited")

        break

    else:

        print("Invalid choice")