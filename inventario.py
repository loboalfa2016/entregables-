# loop indefinitely until a valid product name is received
while True:
    
    # ask the user for the product name and ensure it's treated as a string
    product = str(input("Write the product you want to buy: "))

    # remove spaces and check that all remaining characters are letters
    if product.replace(" ", "").isalpha():
        # valid input; exit the validation loop
        break
    else:
        # feedback if the name contains non-letter characters
        print("Please enter a valid product name (only letters). Try again.")


# loop until a valid positive price is entered
while True:
    try:
        # read input and convert to float; raises ValueError if invalid
        price = float(input("Enter the price of the product")) 

        if price > 0:
            # price is positive, accept it
            break
        else:
            # price zero or negative is not allowed
            print("Error: The price must be greater than 0.")
    except:
        # handle non-numeric input
        print("Error: Enter a valid number for the price.")



# loop until a valid positive integer quantity is entered
while True:
    try:
        # convert input to integer; raises ValueError if not an integer
        quantity = int(input("Enter the quantity of the product to purchase"))

        if quantity > 0:
            # valid quantity provided
            break
        else: 
            # zero or negative quantities are disallowed
            print("Error: The quantity must be greater than 0.")
    except: 
        # caught invalid integer input
        print("Error: The quantity must be a whole number.")




# compute total cost by multiplying price per unit by quantity
costo_total = price * quantity

# display the formatted total cost with two decimal places
print(f"The total cost of / {quantity} / {product}(s)/ is: ${costo_total:.2f}")
