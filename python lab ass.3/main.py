from library_inventory_manager import LibraryInventoryManager
import os

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def show_menu():
    print("" + "="*30)
    print("LIBRARY SYSTEM")
    print("="*30)
    print("1. Add Book")
    print("2. Issue Book") 
    print("3. Return Book")
    print("4. Search Book")
    print("5. Show All Books")
    print("6. Exit")

def main():
    library = LibraryInventoryManager()
    
    while True:
        clear_screen()
        show_menu()
        choice = input("Enter choice: ")
        
        if choice == '1':
            library.add_new_book()
        elif choice == '2':
            library.issue_book()
        elif choice == '3':
            library.return_book()
        elif choice == '4':
            library.search_book()
        elif choice == '5':
            library.display_all()
        elif choice == '6':
            print("Thank you!")
            break
        else:
            print("Wrong choice!")
        
        input("Press Enter to continue...")

if __name__ == "__main__":
    main()


