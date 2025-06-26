#library mangement system
from datetime import datetime, timedelta
from abc import ABC, abstractmethod

class Item(ABC):
    @abstractmethod
    def checkout_item(self):
        pass

    @abstractmethod
    def return_item(self):
        pass

class User(ABC):
    @abstractmethod
    def checkout_item(self):
        pass

    @abstractmethod
    def return_item(self):
        pass

class Book(Item):
    def __init__(self, title, author, item_id):
        self.author = author
        self.title = title
        self.item_id = item_id
        self.checked_out = False
        self.due_date = None
        self.borrower = None

    def checkout_item(self, member_id, days=14):
        if self.checked_out:
            raise ValueError("Item is already checked out")
        
        self.checked_out = True
        self.borrower = member_id
        self.due_date = datetime.now() + timedelta(days=days)
        return True

    def return_item(self):
        self.checked_out = False
        self.due_date = None
        self.borrower = None

    def __str__(self):
        status = "Not Available" if self.checked_out else "Available"
        return f"Item: {self.title} by {self.author} (ID: {self.item_id}) - {status}"

class Member(User):
    def __init__(self, name, member_id):
        self.name = name 
        self.member_id = member_id
        self.items_borrowed = []

    def checkout_item(self, item):
        if len(self.items_borrowed) < 5:
            if item.checkout_item(self.member_id): 
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
        return f"Member: {self.name} (ID: {self.member_id}) - Items borrowed: {len(self.items_borrowed)}"

class Library():
    def __init__(self, name):
        self.name = name
        self.items = []
        self.members = []

    def add_item(self, title, author, item_id):
        new_item = Book(title, author, item_id)
        self.items.append(new_item)
        return new_item

    def add_member(self, name, member_id):
        new_member = Member(name, member_id)
        self.members.append(new_member)
        return new_member
    
    def find_item(self, search_term):
        return [item for item in self.items 
               if (search_term.lower() in item.title.lower() or
                   search_term.lower() in item.author.lower() or
                   search_term == item.item_id)]
            
    def find_member(self, search_term):
        return [member for member in self.members 
               if (search_term.lower() in member.name.lower() or
                   search_term == member.member_id)]
            
    def display_items(self):
        print(f"Items in library: {self.name}")
        for item in self.items:
            print(f"- {item}")

    def display_members(self):
        print(f"Members in library: {self.name}")
        for member in self.members:
            print(f"- {member}")

    def checkout_item(self, member_id, item_id):
        if not (member := next((m for m in self.members if m.member_id == member_id), None)):
            return False
        if not (item := next((i for i in self.items if i.item_id == item_id), None)):
            return False
        return member.checkout_item(item)
        
    def return_item(self, member_id, item_id):
        if not (member := next((m for m in self.members if m.member_id == member_id), None)):
            return False
        if not (item := next((i for i in member.items_borrowed if i.item_id == item_id), None)):
            return False
        item.return_item()
        member.items_borrowed.remove(item)
        return True

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
            member_id = input("Enter member ID: ")
            library.add_member(name, member_id)
            print("Member added successfully!")
        
        elif choice == "3":
            member_id = input("Enter member ID: ")
            item_id = input("Enter item ID: ")
            if library.checkout_item(member_id, item_id):
                print("Item checked out successfully!")
            else:
                print("Could not check out item. Check if member or item exists, or if item is already checked out.")
        
        elif choice == "4":
            member_id = input("Enter member ID: ")
            item_id = input("Enter item ID: ")
            if library.return_item(member_id, item_id):
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