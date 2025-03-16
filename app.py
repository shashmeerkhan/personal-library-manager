import json
import os

# File to store the library data
LIBRARY_FILE = "library.json"

# Load library data from file if exists
def load_library():
    if os.path.exists(LIBRARY_FILE):
        with open(LIBRARY_FILE, "r") as file:
            return json.load(file)
    return []

# Save library data to file
def save_library(library):
    with open(LIBRARY_FILE, "w") as file:
        json.dump(library, file, indent=4)

# Add a book to the library
def add_book(library):
    title = input("Enter the book title: ").strip()
    author = input("Enter the author: ").strip()
    while True:
        try:
            year = int(input("Enter the publication year: "))
            break
        except ValueError:
            print("Please enter a valid year.")
    genre = input("Enter the genre: ").strip()
    read_status = input("Have you read this book? (yes/no): ").strip().lower() == "yes"

    book = {
        "title": title,
        "author": author,
        "year": year,
        "genre": genre,
        "read": read_status
    }
    library.append(book)
    print("Book added successfully!")
    save_library(library)

# Remove a book from the library
def remove_book(library):
    title = input("Enter the title of the book to remove: ").strip()
    for book in library:
        if book["title"].lower() == title.lower():
            library.remove(book)
            print("Book removed successfully!")
            save_library(library)
            return
    print("Book not found.")

# Search for a book by title or author
def search_book(library):
    print("Search by: \n1. Title \n2. Author")
    choice = input("Enter your choice: ").strip()
    keyword = input("Enter the title or author: ").strip().lower()
    
    matches = [book for book in library if keyword in book["title"].lower() or keyword in book["author"].lower()]
    
    if matches:
        print("\nMatching Books:")
        for i, book in enumerate(matches, 1):
            status = "Read" if book["read"] else "Unread"
            print(f"{i}. {book['title']} by {book['author']} ({book['year']}) - {book['genre']} - {status}")
    else:
        print("No matching books found.")

# Display all books in the library
def display_books(library):
    if not library:
        print("Your library is empty.")
        return
    print("\nYour Library:")
    for i, book in enumerate(library, 1):
        status = "Read" if book["read"] else "Unread"
        print(f"{i}. {book['title']} by {book['author']} ({book['year']}) - {book['genre']} - {status}")

# Display library statistics
def display_statistics(library):
    total_books = len(library)
    if total_books == 0:
        print("Your library is empty.")
        return
    read_books = sum(book["read"] for book in library)
    percentage_read = (read_books / total_books) * 100
    print(f"Total books: {total_books}")
    print(f"Percentage read: {percentage_read:.2f}%")

# Menu system
def main():
    library = load_library()

    while True:
        print("\nMenu")
        print("1. Add a book")
        print("2. Remove a book")
        print("3. Search for a book")
        print("4. Display all books")
        print("5. Display statistics")
        print("6. Exit")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            add_book(library)
        elif choice == "2":
            remove_book(library)
        elif choice == "3":
            search_book(library)
        elif choice == "4":
            display_books(library)
        elif choice == "5":
            display_statistics(library)
        elif choice == "6":
            save_library(library)
            print("Library saved to file. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 6.")

if __name__ == "__main__":
    main()
