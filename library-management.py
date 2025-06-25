#library mangement system
class Book():
    def __init__(self, title, author, book_id):
        self.author = author
        self.title = title
        self.book_id = book_id
        self.checked_out = False
        self.due_date = None
        self.borrower = None

    def check_out(self, member, days=14):
        if self.checked_out:
            raise ValueError("book is already checked out")
        
        self.checked_out = True
        self.borrower = member
        self.due_date = None
        return True

    def return_book(self):
        self.checked_out = False
        self.due_date = None
        self.borrower = None

    def __str__(self):
        status = "not Available" if self.checked_out else "Available"
        return f"Book: {self.title} by {self.author} (ID: {self.book_id}) - {status}\n"


class Member():
    def __init__(self, name, member_id):
        self.name = name 
        self.member_id = member_id
        self.books_borrowed = []

    def borrow_book(self, book):
        if len(self.books_borrowed) < 5:
            if book.check_out(self.member_id): 
                self.books_borrowed.append(book)
                return True
        return False


    def return_book(self, book):
        if book in self.books_borrowed:
            book.return_book()
            self.books_borrowed.remove(book)
            return True
        return False

    def __str__(self):
        return f"Member: {self.name}, (ID: {self.member_id}) - Books borrowed: {len(self.books_borrowed)}\n"


class Library():
    def __init__(self, name):
        self.name = name
        self.books = []
        self.members = []

    def add_book(self, title, author, book_id):
        new_book = Book(title, author, book_id)
        self.books.append(new_book)
        return new_book

    def add_member(self, name, member_id):
        new_member = Member(name, member_id)
        self.members.append(new_member)
        return new_member
    
    def find_book(self, search_term):
        result = []
        for book in self.books:
            if (search_term.lower() in book.title.lower() or
                search_term.lower() in book.author.lower() or
                search_term == book.book_id):
                result.append(book)
        return result
            
    def find_member(self, search_term):
        result = []
        for member in self.members:
            if (search_term.lower() in member.name.lower() or
                search_term == member.member_id):
                result.append(member)
        return result
            
    def display_books(self):
        print(f"Books in library: {self.name}\n")
        for book in self.books:
            print(f"- {book}\n")

    def display_members(self):
        print(f"Members in library: {self.name}\n")
        for member in self.members:
            print(f"- {member}\n")

    def checkout_book(self, member_id, book_id):
        member = next((m for m in self.members if m.member_id == member_id), None)
        book = None
        for b in self.books:
            if b.book_id == book_id:
                book = b
            break
        if member and book:
            return member.borrow_book(book)
        
    def return_book(self, member_id, book_id):
        member = next((m for m in self.members if m.member_id == member_id), None)
        if member is None:
            return False
        
        book = next((b for b in member.books_borrowed if b.book_id == book_id), None)
        if book is None:
            return False
        
        book.return_book()
        member.books_borrowed.remove(book)
        return True
        
# display ____________________________________________________________________________________________________________________________
def main_menu(library):
    while True:
        print("\nLibrary Management System")
        print("1. Add a new book")
        print("2. Add a new member")
        print("3. Check out a book")
        print("4. Return a book")
        print("5. Display all books")
        print("6. Display all members")
        print("7. Search for a book")
        print("8. Exit")
        
        choice = input("Enter your choice (1-8): ")
        
        if choice == "1":
            title = input("Enter book title: ")
            author = input("Enter author name: ")
            book_id = input("Enter book ID: ")
            library.add_book(title, author, book_id)
            print("Book added successfully!")
        
        elif choice == "2":
            name = input("Enter member name: ")
            member_id = input("Enter member ID: ")
            library.add_member(name, member_id)
            print("Member added successfully!")
        
        elif choice == "3":
            member_id = input("Enter member ID: ")
            book_id = input("Enter book ID: ")
            if library.check_out_book(member_id, book_id):
                print("Book checked out successfully!")
            else:
                print("Could not check out book. Check if member or book exists, or if book is already checked out.")
        
        elif choice == "4":
            member_id = input("Enter member ID: ")
            book_id = input("Enter book ID: ")
            if library.return_book(member_id, book_id):
                print("Book returned successfully!")
            else:
                print("Could not return book. Check if member or book exists, or if member didn't borrow this book.")
        
        elif choice == "5":
            library.display_books()
        
        elif choice == "6":
            library.display_members()
        
        elif choice == "7":
            search_term = input("Enter book title, author, or ID to search: ")
            results = library.find_book(search_term)
            if results:
                print("\nSearch results:")
                for book in results:
                    print(f"- {book}\n")
            else:
                print("No books found matching your search.")
        
        elif choice == "8":
            print("Goodbye!")
            break
        
        else:
            print("Invalid choice. Please enter a number between 1 and 8.")


if __name__ == "__main__":
    Lib = Library("nerds")

    #adding books ____________________________________________________________________________________________________________________
    Lib.add_book("The Great Gatsby", "F. Scott Fitzgerald", "BK001")
    Lib.add_book("To Kill a Mockingbird", "Harper Lee", "BK002")
    Lib.add_member("John Smith", "MEM001")
    Lib.add_member("Sarah Johnson", "MEM002")
    # ________________________________________________________________________________________________________________________________

    main_menu(Lib)