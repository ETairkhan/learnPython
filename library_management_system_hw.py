books = []

def add_book():
    title = input("Enter book title: ").strip()
    author = input("Enter author name: ").strip()

    # Loop until the user enters a valid year
    while True:
        year = input("Enter year of publication: ").strip()
        if not year.isdigit() or int(year) <= 0:
            print("Year must be a positive integer. Please try again.")
        else:
            year = int(year)
            break

    # Loop until the user enters a valid number of copies
    while True:
        copies = input("Enter number of copies: ").strip()
        if not copies.isdigit() or int(copies) < 0:
            print("Copies must be a non-negative integer. Please try again.")
        else:
            copies = int(copies)
            break

    # Check if the book already exists and update copies if it does
    for book in books:
        if book['title'].lower() == title.lower():
            book['copies_available'] += copies
            print(f"Updated copies for '{title}'.")
            return

    # Add the new book to the library
    books.append({
        'title': title,
        'author': author,
        'year': year,
        'copies_available': copies
    })
    print(f"Book '{title}' added successfully.")

def search_book():
    title = input("Enter the title of the book to search: ").strip()
    for book in books:
        if book['title'].lower() == title.lower():
            print(f"\nTitle: {book['title']}\nAuthor: {book['author']}\nYear: {book['year']}\nCopies Available: {book['copies_available']}")
            return
    print("The book was not found.")

def borrow_book():
    title = input("Enter the title of the book to borrow: ").strip()
    for book in books:
        if book['title'].lower() == title.lower():
            if book['copies_available'] > 0:
                book['copies_available'] -= 1
                print(f"You have successfully borrowed '{title}'.")
                return
            else:
                print("No copies available to borrow.")
                return
    print("The book was not found.")

def return_book():
    title = input("Enter the title of the book to return: ").strip()
    for book in books:
        if book['title'].lower() == title.lower():
            book['copies_available'] += 1
            print(f"You have successfully returned '{title}'.")
            return
    print("The book was not found.")

def view_all_books():
    if not books:
        print("No books in the library.")
        return
    print(f"{'Title':<30} {'Author':<20} {'Year':<10} {'Copies':<10}")
    print("-" * 70)
    for book in books:
        print(f"{book['title']:<30} {book['author']:<20} {book['year']:<10} {book['copies_available']:<10}")

def main():
    while True:
        print("\nLibrary Management System")
        print("1. Add a Book")
        print("2. Search for a Book")
        print("3. Borrow a Book")
        print("4. Return a Book")
        print("5. View All Books")
        print("6. Exit")
        choice = input("Enter your choice: ").strip()
        if choice == '1':
            add_book()
        elif choice == '2':
            search_book()
        elif choice == '3':
            borrow_book()
        elif choice == '4':
            return_book()
        elif choice == '5':
            view_all_books()
        elif choice == '6':
            print("Exiting the Library Management System. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
