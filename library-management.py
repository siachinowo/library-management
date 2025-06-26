#library mangement system
from datetime import datetime, timedelta
from abc import ABC
import uuid

# Items ______________________________________________________________________________________________________________________________
class Item(ABC):
    def __init__(self, title, creator, item_id):
        self.title = title
        self.creator = creator
        self.item_id = item_id
        self.checked_out = False
        self.due_date = None
        self.borrower = None

    def checkout_item(self, user_id, days=14):
        if self.checked_out:
            raise ValueError("Item is already checked out")
        
        self.checked_out = True
        self.borrower = user_id
        self.due_date = datetime.now() + timedelta(days=days)
        return True

    def return_item(self):
        self.checked_out = False
        self.due_date = None
        self.borrower = None

    def __str__(self):
        status = "Not Available" if self.checked_out else "Available"
        return (f"{self.__class__.__name__}: {self.title} "
                f",{self.creator_role}: {self.creator}"
                f"(ID:{self.item_id} - {status}")

class Book(Item):
    @property
    def creator_role(self):
        return "Author"
    
class ComicBook(Item):
    @property
    def creator_role(self):
        return "Artist"
   
class DVD(Item):
    @property
    def creator_role(self):
        return "Director"

# users ___________________________________________________________________________________________________________________________
class User(ABC):
    def __init__(self, name, user_id):
        self.name = name 
        self.user_id = user_id
        self.items_borrowed = []
        self.access_level = "not restricted"
        self.max_items = 5  
        self.loan_days = 14

    def checkout_item(self, item):
        if len(self.items_borrowed) < self.max_items:
            if item.checkout_item(self.user_id): 
                self.items_borrowed.append(item)
                return True
        return False

    def return_item(self, item):
        if item in self.items_borrowed:
            item.return_item()
            self.items_borrowed.remove(item)
            return True
        return False
    
    def __str__(self):
        return f"{self.__class__.__name__} Account: {self.name} (ID: {self.user_id}) - Items borrowed: {len(self.items_borrowed)}"

class Member(User):
    pass
       
class Guest(User):
    def __init__(self):
        super().__init__(name="Guest", user_id=f"GUEST_{uuid.uuid4().hex[:3]}")
        self.access_level = "restricted"
        self.max_items = 1  
        self.loan_days = 7


# Library _____________________________________________________________________________________________________________________
class Library():
    def __init__(self, name):
        self.name = name

        self.books = []
        self.comics = []
        self.dvds = []

        self.members = []
        self.guests = []

    # add item ____________________________________________
    def add_book(self, title, author, item_id):
        new_item = Book(title, author, item_id)
        self.books.append(new_item)
        return new_item
    
    def add_comic(self, title, artist, item_id):
        new_item = ComicBook(title, artist, item_id)
        self.comics.append(new_item)
        return new_item
    
    def add_dvd(self, title, director, item_id):
        new_item = DVD(title, director, item_id)
        self.dvds.append(new_item)
        return new_item

    # add user _____________________________________________
    def add_member(self, name, user_id):
        new_user = Member(name, user_id)
        self.members.append(new_user)
        return new_user
    
    def add_guest(self, name, user_id):
        new_user = Guest(name, user_id)
        self.guests.append(new_user)
        return new_user
    
    def find_item(self, search_term):
        return [item for item in (self.books + self.comics + self.dvds) 
               if (search_term.lower() in item.title.lower() or
                   search_term.lower() in item.author.lower() or
                   search_term == item.item_id)]
            
    def find_user(self, search_term):
        return [user for user in (self.members + self.guests)
            if (search_term.lower() in user.name.lower() or
                search_term == user.user_id)]
            
    def display_items(self):
        print(f"Items in library: {self.name}")
        for item in self.items:
            print(f"- {item}")

    def display_user(self):
        print(f"Members in library: {self.name}")
        for user in self.members:
            print(f"- {user}")

    def checkout_item(self, user_id, item_id):
        if not (member := next((m for m in self.members if m.user_id == user_id), None)):
            return False
        if not (item := next((i for i in self.items if i.item_id == item_id), None)):
            return False
        return member.checkout_item(item)
        
    def return_item(self, user_id, item_id):
        if not (member := next((m for m in self.members if m.user_id == user_id), None)):
            return False
        if not (item := next((i for i in member.items_borrowed if i.item_id == item_id), None)):
            return False
        item.return_item()
        member.items_borrowed.remove(item)
        return True

# display ____________________________________________________________________________________________________________________
def main_menu(library):
    while True:
        print("\nLibrary Management System")
        print("1. Add a new item")
        print("2. Add a new member")
        print("3. Check out an item")
        print("4. Return an item")
        print("5. Display all items")
        print("6. Display all members")
        print("7. Search for an item")
        print("8. Exit")
        
        choice = input("Enter your choice (1-8): ")

        if choice == "1":
            title = input("Enter item title: ")
            author = input("Enter author name: ")
            item_id = input("Enter item ID: ")
            library.add_item(title, author, item_id)
            print("Item added successfully!")
        
        elif choice == "2":
            name = input("Enter member name: ")
            user_id = input("Enter user ID: ")
            library.add_member(name, user_id)
            print("Member added successfully!")
        
        elif choice == "3":
            user_id = input("Enter user ID: ")
            item_id = input("Enter item ID: ")
            if library.checkout_item(user_id, item_id):
                print("Item checked out successfully!")
            else:
                print("Could not check out item. Check if member or item exists, or if item is already checked out.")
        
        elif choice == "4":
            user_id = input("Enter user ID: ")
            item_id = input("Enter item ID: ")
            if library.return_item(user_id, item_id):
                print("Item returned successfully!")
            else:
                print("Could not return item. Check if member or item exists, or if member didn't borrow this item.")
        
        elif choice == "5":
            library.display_items()
        
        elif choice == "6":
            library.display_members()
        
        elif choice == "7":
            search_term = input("Enter item title, author, or ID to search: ")
            if results := library.find_item(search_term):
                print("Search results:")
                for item in results:
                    print(f"- {item}")
            else:
                print("No items found matching your search.")
        
        elif choice == "8":
            print("Thank you for visiting our (fake) library! :D")
            break
        
        else:
            print("Invalid choice. Please enter a number between 1 and 8.")

if __name__ == "__main__":
    Lib = Library("nerds")

#adding books and members ________________________________________________________________________________________________________
    Lib.add_book("The Great Gatsby", "F. Scott Fitzgerald", "BK001")
    Lib.add_book("To Kill a Mockingbird", "Harper Lee", "BK002")

    Lib.add_member("Harrum Fatima", "MEM001")
    Lib.add_member("Siachin", "MEM002")
    # ____________________________________________________________________________________________________________________________

    main_menu(Lib)