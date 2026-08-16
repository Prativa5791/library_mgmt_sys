from library import Library

lib = Library()

while True:
    print("\nLibrary Management System")
    print("1. Add Book")
    print("2. Register Member")
    print("3. Issue Book")
    print("4. Return Book")
    print("5. Search Book")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == '1':
        try:
            isbn = input("Enter ISBN: ")
            title = input("Enter Title: ")
            author = input("Enter Author: ")
            total_copies = int(input("Enter Total Copies: "))
            lib.add_book(isbn, title, author, total_copies)
            print(f"Book '{title}' added successfully.")
        except ValueError as exc:
            print(exc)

    elif choice == '2':
        try:
            member_id = input("Enter Member ID: ")
            name = input("Enter Name: ")
            member_type = input("Enter Member Type (student/faculty): ")
            lib.register_member(member_id, name, member_type)
            print(f"Member '{name}' registered successfully.")
        except ValueError as exc:
            print(exc)

    elif choice == '3':
        try:
            isbn = input("Enter ISBN of the book to issue: ")
            member_id = input("Enter Member ID: ")
            lib.issue_book(isbn, member_id)
            print("Book issued successfully.")
        except ValueError as exc:
            print(exc)

    elif choice == '4':
        try:
            isbn = input("Enter ISBN of the book to return: ")
            member_id = input("Enter Member ID: ")
            lib.return_book(isbn, member_id)
            print("Book returned successfully.")
        except ValueError as exc:
            print(exc)

    elif choice == '5':
        search_term = input("Enter title or author to search: ")
        results = lib.search_books(search_term=search_term)
        if results:
            print("Search Results:")
            for book in results:
                print(book)
        else:
            print("Book not found")

    elif choice == '6':
        print("Exiting the system.")
        break

    else:
        print("Invalid choice. Please try again.")
