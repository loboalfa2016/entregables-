import csv

def save_csv(inventory, path):
    if not inventory:
        print("The inventory is empty.")
        return
    confirmation = input(f"Do you want to overwrite the file {path}? (y/n)")
    if confirmation.upper() != "Y":
        print("Operation cancelled.")
        return
    try:
        with open(path, "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["name", "price", "quantity"])
            for product in inventory:
                writer.writerow([product["name"], product["price"], product["quantity"]])
            print(f"Inventory saved successfully in {path}.")
    except Exception as e:
        print(f"Error saving inventory: {e}")

def load_csv(path):
    try:
        with open(path, "r") as file:
            reader = csv.DictReader(file)
            inventory = []
            for row in reader:
                name, price, quantity = row["name"], float(row["price"]), int(row["quantity"])
                inventory.append({"name": name, "price": price, "quantity": quantity})
            print(f"Inventory loaded successfully from {path}.")
            return inventory
    except Exception as e:
        print(f"Error loading inventory: {e}")
        return []
