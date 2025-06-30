from read import load_products_from_file
from operations import buy_products, restock_products

# Initial welcome print statements
print("\n" * 2)
print("\t" * 7 + "WeCare Store\n")
print("\t" * 5 + "Newroad, Kathmandu | Phone No: 9813844416\n")
print("-" * 117)
print("\t" * 4 + "Welcome to the system Admin! I hope you have a good day ahead!")
print("-" * 117 + "\n")

# Main program
products = load_products_from_file()

#Menu loop
while True:
    print("\n1. View Products")
    print("2. Buy Products")
    print("3. Restock Product")
    print("4. Exit")
    choice = input("Choose an option: ")

    if choice == '1':
        print()
        print("Product Name" + " " * (24 - len("Product Name")) + "| " +"Brand" + " " * (20 - len("Brand")) + "| " +" " * (9 - len("Quantity")) + "Quantity | " +" " * (7 - len("Price")) + "Price | Country")
        print("-" * 83)

        for p in products:
            name = p[0] + " " * (24 - len(p[0]))
            brand = p[1] + " " * (20 - len(p[1]))
            qty = " " * (9 - len(str(p[2]))) + str(p[2])
            price = " " * (7 - len(str(p[3]))) + str(p[3])
            print(name + "| " + brand + "| " + qty + " | " + price + " | " + p[4])

    elif choice == '2':
        buy_products(products)

    elif choice == '3':
        restock_products(products)

    elif choice == '4':
        print("Thank you for using WeCare Store system. Goodbye!")
        break

    else:
        print("Invalid input. Please try again.")
