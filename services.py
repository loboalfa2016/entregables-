def add_product(inventory, name, price, quantity):
    inventory.append({"name": name, "price": price, "quantity": quantity})
    print(f"Product '{name}' added successfully.")

def show_inventory(inventory):
    if not inventory:
        print("The inventory is empty.")
    else:
        for product in inventory:
            print(f"Name: {product['name']}, Price: {product['price']}, Quantity: {product['quantity']}")

def find_product(inventory, name):
    for product in inventory:
        if product["name"].lower() == name.lower():
            return product
    return None

def delete_product(inventory, name):
    product = find_product(inventory, name)
    if not product:
        print(f"Product '{name}' not found.")
        return
    else: 
        inventory.remove(product)
        print(f"Product {name} deleted successfully.")

def update_product(inventory, name, price=None, quantity=None):
    product = find_product(inventory, name)
    if not product:
        print(f"Product {name} not found.")
        return
    if price:
        product["price"] = price
        print(f"Price of product {name} updated successfully.")
    if quantity:
        product["quantity"] = quantity
        print(f"Quantity of product {name} updated successfully.")

def calculate_statistics(inventory):
    if not inventory:
        print("The inventory is empty.")
        return None
    total_units = sum(product["quantity"] for product in inventory)
    total_value = sum(product["price"] * product["quantity"] for product in inventory)
    most_expensive_product = max(inventory, key=lambda x: x["price"])
    highest_stock_product = max(inventory, key=lambda x: x["quantity"])
    return {
        "total_units": total_units,
        "total_value": total_value,
        "most_expensive_product": most_expensive_product,
        "highest_stock_product": highest_stock_product
    }
