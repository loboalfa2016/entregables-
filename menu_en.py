import services
import files
import re

def main():
    inventory = []
    
    while True:
        print("\nMain Menu")
        print("1. Add product")
        print("2. Show inventory")
        print("3. Find product")
        print("4. Update product")
        print("5. Delete product")
        print("6. Calculate statistics")
        print("7. Save CSV")
        print("8. Load CSV")
        print("9. Exit")
        option = input("Enter an option: ")

        if not option.isdigit() or not 1 <= int(option) <= 9:
            print("Invalid option")
            continue

        match int(option):
            case 1:
                name = input("Enter the product name: ")
                while not re.match("^[a-zA-Z0-9 ]+$", name):
                    print("Invalid name. Please enter a name that only contains letters, numbers and spaces.")
                    name = input("Enter the product name: ")

                while True:
                    try:
                        price = float(input("Enter the product price: "))
                        if price <= 0:
                            print("Invalid price. Please enter a positive price.")
                        else:
                            break
                    except ValueError:
                        print("Invalid price. Please enter a number.")

                while True:
                    try:
                        quantity = int(input("Enter the product quantity: "))
                        if quantity <= 0:
                            print("Invalid quantity. Please enter a positive quantity.")
                        else:
                            break
                    except ValueError:
                        print("Invalid quantity. Please enter an integer number.")

                services.add_product(inventory, name, price, quantity)

            case 2:
                services.show_inventory(inventory)

            case 3:
                name = input("Enter the product name: ")
                while not re.match("^[a-zA-Z0-9 ]+$", name):
                    print("Invalid name. Please enter a name that only contains letters, numbers and spaces.")
                    name = input("Enter the product name: ")

                product = services.find_product(inventory, name)
                if product:
                    print(product)
                else:
                    print("Product not found")

            case 4:
                name = input("Enter the product name: ")
                while not re.match("^[a-zA-Z0-9 ]+$", name):
                    print("Invalid name. Please enter a name that only contains letters, numbers and spaces.")
                    name = input("Enter the product name: ")

                while True:
                    try:
                        new_price = float(input("Enter the new product price: "))
                        if new_price <= 0:
                            print("Invalid price. Please enter a positive price.")
                        else:
                            break
                    except ValueError:
                        print("Invalid price. Please enter a number.")

                while True:
                    try:
                        new_quantity = int(input("Enter the new product quantity: "))
                        if new_quantity <= 0:
                            print("Invalid quantity. Please enter a positive quantity.")
                        else:
                            break
                    except ValueError:
                        print("Invalid quantity. Please enter an integer number.")

                services.update_product(inventory, name, new_price, new_quantity)

            case 5:
                name = input("Enter the product name: ")
                while not re.match("^[a-zA-Z0-9 ]+$", name):
                    print("Invalid name. Please enter a name that only contains letters, numbers and spaces.")
                    name = input("Enter the product name: ")

                services.delete_product(inventory, name)

            case 6:
                statistics = services.calculate_statistics(inventory)
                print(statistics)

            case 7:
                path = input("Enter the CSV file path: ")
                while not path.endswith(".csv"):
                    print("Invalid path. Please enter a path that ends with .csv")
                    path = input("Enter the CSV file path: ")

                files.save_csv(inventory, path)

            case 8:
                path = input("Enter the CSV file path: ")
                while not path.endswith(".csv"):
                    print("Invalid path. Please enter a path that ends with .csv")
                    path = input("Enter the CSV file path: ")

                inventory = files.load_csv(path)

            case 9:
                break

            case _:
                print("Invalid option")
