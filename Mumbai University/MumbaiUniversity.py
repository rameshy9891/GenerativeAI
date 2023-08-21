# Snack inventory data structure (list of dictionaries)
snack_inventory = []

# Sales records data structure (dictionary)
sales_records = {}

def add_snack():
    # Function to add a snack to the inventory
    print("\n--- Add a Snack to Inventory ---")
    try:
        snack_id = input("Enter snack ID: ")
        snack_name = input("Enter snack name: ")
        snack_price = float(input("Enter snack price: "))
        snack_available = input("Is the snack available? (yes/no): ").lower()

        snack = {
            "id": snack_id,
            "name": snack_name,
            "price": snack_price,
            "available": snack_available == "yes"
        }

        snack_inventory.append(snack)
        print(f"Snack {snack_name} (ID: {snack_id}) added to inventory.")
    except ValueError:
        print("Invalid input. Please enter valid details.")

def remove_snack():
    # Function to remove a snack from the inventory
    print("\n--- Remove a Snack from Inventory ---")
    snack_id = input("Enter the snack ID to remove: ")

    for snack in snack_inventory:
        if snack["id"] == snack_id:
            snack_inventory.remove(snack)
            print(f"Snack with ID {snack_id} removed from inventory.")
            return

    print(f"Snack with ID {snack_id} not found in inventory.")

def update_availability():
    # Function to update the availability of a snack
    print("\n--- Update Snack Availability ---")
    snack_id = input("Enter the snack ID to update availability: ")

    for snack in snack_inventory:
        if snack["id"] == snack_id:
            new_availability = input("Is the snack available now? (yes/no): ").lower()
            snack["available"] = new_availability == "yes"
            print(f"Snack with ID {snack_id} availability updated.")
            return

    print(f"Snack with ID {snack_id} not found in inventory.")

def record_sale(snack_id):
    # Function to record a sale of a snack
    if snack_id in sales_records:
        sales_records[snack_id] += 1
    else:
        sales_records[snack_id] = 1

    for snack in snack_inventory:
        if snack["id"] == snack_id:
            snack["available"] = False
            print(f"Sale of Snack {snack['name']} (ID: {snack_id}) recorded.")
            return

    print(f"Snack with ID {snack_id} not found in inventory.")

def display_inventory():
    # Function to display the current snack inventory
    print("\n--- Snack Inventory ---")
    for snack in snack_inventory:
        print(f"ID: {snack['id']}, Name: {snack['name']}, Price: {snack['price']}, Available: {snack['available']}")

def display_sales_records():
    # Function to display the sales records
    print("\n--- Sales Records ---")
    for snack_id, count in sales_records.items():
        for snack in snack_inventory:
            if snack["id"] == snack_id:
                print(f"Snack: {snack['name']} (ID: {snack_id}), Quantity Sold: {count}")
# ... (previous code remains the same)

def main():
    while True:
        print("\n---- Mumbai Munchies Canteen Management System ----")
        print("1. Add a snack to the inventory")
        print("2. Remove a snack from the inventory")
        print("3. Update the availability of a snack")
        print("4. Record a sale")
        print("5. Display snack inventory")
        print("6. Display sales records")
        print("7. Exit")

        choice = input("Enter your choice (1-7): ").strip()

        if choice == "1":
            add_snack()
        elif choice == "2":
            remove_snack()
        elif choice == "3":
            update_availability()
        elif choice == "4":
            snack_id = input("Enter the snack ID sold: ").strip()
            record_sale(snack_id)
        elif choice == "5":
            display_inventory()
        elif choice == "6":
            display_sales_records()
        elif choice == "7":
            print("Exiting Mumbai Munchies Canteen Management System. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a valid option (1-7).")

if __name__ == "__main__":
    main()
