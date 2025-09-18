from members import add_member, update_member, delete_member, list_members
from books import add_book, update_book, delete_book, list_books, search_books
from borrows import borrow_book, return_book, overdue_books

def menu():
    print("""
    1. Add Member
    2. Update Member
    3. Delete Member
    4. List Members
    5. Add Book
    6. Update Book
    7. Delete Book
    8. List Books
    9. Search Books
    10. Borrow Book
    11. Return Book
    12. Overdue Books
    13. Exit
    """)
    choice = input("Enter choice: ")
    return choice

if __name__ == "__main__":
    while True:
        choice = menu()
        if choice == "1":
            add_member(input("Name: "), input("Email: "))
        elif choice == "2":
            update_member(int(input("Member ID: ")), input("Name (leave blank to skip): "), input("Email (leave blank to skip): "))
        elif choice == "3":
            delete_member(int(input("Member ID: ")))
        elif choice == "4":
            list_members()
        elif choice == "5":
            add_book(input("Title: "), input("Author: "), input("Category: "), int(input("Stock: ")))
        elif choice == "6":
            update_book(int(input("Book ID: ")), input("Title: "), input("Author: "), input("Category: "), input("Stock: ") or None)
        elif choice == "7":
            delete_book(int(input("Book ID: ")))
        elif choice == "8":
            list_books()
        elif choice == "9":
            search_books(input("Keyword: "))
        elif choice == "10":
            borrow_book(int(input("Member ID: ")), int(input("Book ID: ")))
        elif choice == "11":
            return_book(int(input("Record ID: ")))
        elif choice == "12":
            overdue_books()
        elif choice == "13":
            break
        else:
            print("Invalid choice!")
