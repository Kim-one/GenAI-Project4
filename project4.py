# Project 4: Impleting Data Structures
# This program creates a simple inventory management program using lists, dictionaries an tuples

# Creates an empty dictionary
inventory = {}

print("**********************************************")
print("\tWelcome to Inventory Manager")

# Initialize the dictionary 
inventory = {
    "apple": (10, 2.5),
    "banana": (20, 1.2)
}

# Displays the current inventory
def display():
    print("Current Inventory:")
    for item, (quantity, price) in inventory.items():
        print(f"Item: {item}, Quantity: {quantity}, Price: ${price}")

# Continuously prompts the user for the inventory 
while(True):
    # # Displays the inventory 
    # display()

    # Displays a menu of options for user input
    option = int(input("\n1. Add\n2. Update\n3. Remove\n4. View All\n5. Calculate Total\n6. Exit -> "))

    # Add a new item to the dictionary
    if option == 1:
        print("\n------------------Adding Item------------------")
        item = input("Enter item: ")
        quantity = int(input("Enter quantity: "))
        price = float(input("Enter price: "))
        inventory.update({item:(quantity,price)})
        display()
        print(f"Adding a new item: {item}")
    # Update an item in the inventory based on item name
    elif option == 2:
        print("\n---------------Updating Item-----------------")
        item = input("Enter item name to update: ")
        if item in inventory:
            quantity = int(input("Enter new quantity: "))
            price = float(input("Enter new price: "))
            inventory[item] = (quantity, price)
            print(f"Updated Inventory: ")
            display()
        else:
            print(f"{item} not found!")
    # Remove an item from the dictionary based on item name 
    elif option == 3:
        print("\n--------------Deleting Item----------------")
        item = input("Enter item name to delete: ")
        if item in inventory:
            inventory.pop(item)
            print(f"Deleted Item: {item}")
        else:
            print(f"{item} not found!")
    # View the current inventory
    elif option == 4:
        display()
    # Calculate the total value of the inventory 
    elif option == 5:
        total = sum(quantity*price for quantity, price in inventory.values())
        print(f"\nTotal value of inventory: ${price}")
    # Exit the loop and program 
    elif option == 6:
        exit()