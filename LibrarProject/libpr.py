from zoneinfo import available_timezones
import mysql.connector
from datetime import datetime


# Function to establish a connection to MySQL
def create_connection():
    connection = mysql.connector.connect(
        host="localhost",
        user="rooter",
        password="admin",
        database="bms"
    )
    return connection
# Function to create a books table
def create_books_table(connection):
    cursor = connection.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS books (
            id INT AUTO_INCREMENT PRIMARY KEY,
            title VARCHAR(255),
            author VARCHAR(255),
            available BOOLEAN
        )
    """)
    connection.commit()

# Function to add a book to the library
def add_book(connection, title, author):
    cursor = connection.cursor()
    cursor.execute("INSERT INTO books (title, author, available) VALUES (%s, %s, %s)", (title, author, True))
    connection.commit()

# Function to update a book
def Update_books(connection, title,author,available,book_id):
    cursor = connection.cursor()
    cursor.execute("UPDATE books SET title=%s, author=%s,available=%s WHERE id = %s", (title,author,available,book_id,))
    connection.commit()

# Function to display all books in the library
def display_books(connection):
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM books")
    books = cursor.fetchall()

    if not books:
        print("No books available.")
    else:
        print("Library Books:")
        for book in books:
            print(f"ID: {book[0]}, Title: {book[1]}, Author: {book[2]}, Available: {'Yes' if book[3] else 'No'}")

# Function to delete a book from the library
def delete_book(connection, book_id):
    cursor = connection.cursor()
    cursor.execute("DELETE FROM books WHERE id = %s", (book_id,))
    connection.commit()

# Main function to demonstrate the library management system
def main():
    connection = create_connection()
    create_books_table(connection)

    while True:
        print("\nLibrary Management System:")
        print("1. Add Book")
        print("2. Update Books")
        print("3. Display Books")
        print("4. Delete Book")
        print("0. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            title = input("Enter book title: ")
            author = input("Enter book author: ")
            add_book(connection, title, author)
            print("Book added successfully")

        elif choice == "2":
            book_id = int(input("Enter the book ID to update: "))
            title = input("Enter new title: ")
            author = input("Enter new author: ")
            available = input("Enter new availability: ")
            Update_books(connection, title, author, available, book_id)
            print("Book updated successfully")

        elif choice == "3":
            display_books(connection)
            
        elif choice == "4":
            book_id = int(input("Enter the ID of the book to delete: "))
            delete_book(connection, book_id)
        elif choice == "0":
            break
        else:
            print("Invalid choice. Please try again.")

    connection.close()

if __name__ == "__main__":
    main()




