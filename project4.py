# Step 1
inventory = {}

print("**********************************************")
print("\tWelcome to Inventory Manager")

inventory = {
    "apple": (10, 2.5),
    "banana": (20, 1.2)
}


while(True):
    
    option = int(input("1. Add\n2. Update\n3. Remove\n4. View All\n5. Calculate Total\n6. Exit -> "))
    if option == 1:
        item = input("Enter item: ")
        quantity = int(input("Enter quantity: "))
        price = float(input("Enter price: "))
        inventory.update({item:(quantity,price)})
        print(f"Added Item: {item}")
    elif option == 2:
        item = input("Enter item name to update: ")
        if item in inventory:
            quantity = int(input("Enter new quantity: "))
            price = float(input("Enter new price: "))
            inventory[item] = (quantity, price)
            print(f"Updated Inventory: {inventory}")
        else:
            print("Item not found!")
    elif option == 3:
        item = input("Enter item name to delete: ")
        inventory.pop(item)
        print(f"Deleted Item: {item}")
    elif option == 4:
        print("Current Inventory:")
        for item, (quantity, price) in inventory.items():
            print(f"Item: {item}, Quantity: {quantity}, Price: ${price}")
    elif option == 5:
        total = sum(quantity*price for quantity, price in inventory.values())
        print(f"Total value of inventory: ${price}")
    elif option == 6:
        exit()

    
