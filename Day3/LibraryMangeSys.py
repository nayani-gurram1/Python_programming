library={}
while True:
    print("\nLibrary Operations:")
    print("1. Add Book")
    print("2. Remove Book")
    print("3. Search Book by ID")
    print("4. Update Book Title")
    print("5. Display All Books")
    print("6. Count Total Books")
    print("7. Check if Book Title Exists")
    print("8. Exit")
    choice=int(input("\nEnter your choice: "))
    if choice==1:
        book_id=input("Enter Book ID: ")
        title=input("Enter Book Title: ")
        library[book_id]=title
        print(f"Book '{title}' added with ID {book_id}.")
    elif choice==2:
        book_id=input("Enter Book ID to remove: ")
        if book_id in library:
            removed=library.pop(book_id)
            print(f"Book '{removed}' with ID {book_id} removed.")
        else:
            print("Book ID not found.")
    elif choice==3:
        book_id=input("Enter Book ID to search: ")
        if book_id in library:
            print(f"Book found: {library[book_id]}")
        else:
            print("Book ID not found.")
    elif choice==4:
        book_id=input("Enter Book ID to update: ")
        if book_id in library:
            new_title=input("Enter new Book Title: ")
            library[book_id]=new_title
            print(f"Book ID {book_id} updated to '{new_title}'.")
        else:
            print("Book ID not found.")
    elif choice==5:
        if library:
            print("All books in the library:")
            for book_id, title in library.items():
                print(f"ID: {book_id}, Title: {title}")
        else:
            print("Library is empty.")
    elif choice==6:
        print(f"Total number of books: {len(library)}")
    elif choice==7:
        title_check=input("Enter Book Title to check: ")
        if title_check in library.values():
            print(f"Book title '{title_check}' exists in the library.")
        else:
            print(f"Book title '{title_check}' does NOT exist.")
    elif choice==8:
        print("Exiting the Library Management System...")
        break
    else:
        print("Invalid choice! Try again.")