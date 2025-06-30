from write import save_sale_invoice, save_restock_invoice, write_products_to_file
#function to buy products
def buy_products(products):
    """
    Handles the product purchasw process, updates the inventory, calculates the total cost, and generates a sales invoice.

    Parameters:
    products(list): A list of products where each product is a list containingname, brand, quantity, selling price, and country.

    Prompts the user for their name, allows them to select products to buy, applies a buy-2-get-1-free offer, updates stock, and generates an invoice.

    Returns:
        None
    """
    bought_items = []
    total = 0
    total_free_items = 0

    user_name = input("Enter your name: ")

    while True:
        print("\nAvailable Products:")
        print("ID" + " " * (4 - len("ID")) +"Product Name" + " " * (24 - len("Product Name")) + "| " +"Brand" + " " * (20 - len("Brand")) + "| " +" " * (9 - len("Quantity")) + "Quantity | " +" " * (7 - len("Price")) + "Price | Country")
        print("-" * 83)

        for i in range(len(products)):
            p = products[i]
            index = str(i + 1)
            name = p[0] + " " * (24 - len(p[0]))
            brand = p[1] + " " * (20 - len(p[1]))
            qty = " " * (9 - len(p[2])) + p[2]
            price = " " * (7 - len(p[3])) + p[3]
            print(index + " " * (4 - len(index)) + name + "| " + brand + "| " + qty + " | " + price + " | " + p[4])
            print("-" * 83)

        try:
            product_id = input("Enter product ID to buy (or 'done' to finish): ")
            if product_id.lower() == 'done':
                break

            product_id = int(product_id) - 1
            if not (0 <= product_id < len(products)):
                print("Invalid product ID!")
                continue

            quantity = int(input("Enter quantity: "))
            if quantity <= 0:
                print("Quantity must be positive!")
                continue

            available_qty = int(products[product_id][2])
            if quantity > available_qty:
                print("Only " + str(available_qty) + " available!")
                continue

            #Update the product quantity
            products[product_id][2] = str(available_qty - quantity)
            #Add to the bought items
            price = products[product_id][3]
            item_total = quantity * int(price)
            total += item_total

            bought_items.append({
                'name': products[product_id][0],
                'quantity': quantity,
                'price': price
            })

            #Check for free items
            free_items = quantity // 3
            if free_items:
                total_free_items += free_items
                print("Congratulations! You get " + str(total_free_items) + " free items!")

            print("Added " + str(quantity) + " x " + products[product_id][0] + " to your cart.")

        except ValueError:
            print("Invalid input! Please enter numbers only.")

    if bought_items:
        print("\nYour purchase summary:")
        for item in bought_items:
            print(item['name'] + ": " + str(item['quantity']) + " x " + str(item['price']) + " = " + str(item['quantity'] * int(item['price'])))

        print("-" * 75)
        print("Total: " + str(total))
        print("-" * 75)

        if total_free_items:
            print("\nYou got " + str(total_free_items) + " free items!")

        save_sale_invoice(user_name, bought_items, total, total_free_items)
        write_products_to_file("products.txt", products)
        print("\nInvoice saved successfully!")
    else:
        print("No items were purchased.")

#function to restock products
def restock_products(products):
    """
        Handles the restock process of products, calculates the costs, and generates a restocking invoice.

    Parameters:
        products(list): A list of product lists, each containing: [name, brand, quantity, selling_price, country].

        Prompts the supplier for name, product to restock, and quantity.
        Updates product stock, calculates total cost, and prints invoice.

    Returns:
        None
    """
    restock_items = []
    total_cost = 0

    supplier_name = input("Enter supplier name: ")
    if not supplier_name:
        print("Supplier name cannot be empty!")
        return

    while True:
        print("\nAvailable Products:")
        print("ID" + " " * (4 - len("ID")) +"Product Name" + " " * (24 - len("Product Name")) + "| " +"Brand" + " " * (20 - len("Brand")) + "| " +" " * (9 - len("Quantity")) + "Quantity | " +" " * (7 - len("Price")) + "Price | Country")
        print("-" * 83)

        for i in range(len(products)):
            p = products[i]
            index = str(i + 1)
            name = p[0] + " " * (24 - len(p[0]))
            brand = p[1] + " " * (20 - len(p[1]))
            qty = " " * (9 - len(p[2])) + p[2]
            price = " " * (7 - len(p[3])) + p[3]
            print(index + " " * (4 - len(index)) + name + "| " + brand + "| " + qty + " | " + price + " | " + p[4])
            print("-" * 83)

        try:
            product_id = input("Enter product ID to restock (or 'done' to finish): ")
            if product_id.lower() == 'done':
                break

            product_id = int(product_id) - 1
            if not (0 <= product_id < len(products)):
                print("Invalid product ID!")
                continue

            #selling price is 2 times the cost
            current_cost = int(products[product_id][3]) // 2
            print("Current cost price: Rs. " + str(current_cost))

            new_cost = input("Enter new cost price (or press Enter to keep Rs. " + str(current_cost) + "): ")
            cost_price = int(new_cost) if new_cost else current_cost

            quantity = int(input("Enter restock quantity: "))
            if quantity <= 0:
                print("Quantity must be positive!")
                continue

            #Update the product details
            products[product_id][2] = str(int(products[product_id][2]) + quantity)
            products[product_id][3] = str(cost_price * 2)

            #Calculate item total
            item_total = quantity * cost_price
            total_cost += item_total

            restock_items.append({
                'name': products[product_id][0],
                'brand': products[product_id][1],
                'quantity': quantity,
                'cost_price': cost_price,
                'subtotal': item_total
            })

            print("Added " + str(quantity) + " " + products[product_id][0] + " to restock list")

        except ValueError:
            print("Invalid input! Please enter numbers only.")

    if restock_items:
        vat = int(total_cost*13/100)
        grand_total = total_cost+vat
        print("\nRestock Summary:")
        print("Product Name             Brand               Qty   | Cost Price  | Subtotal")
        print("-" * 75)

    for item in restock_items:
         name = item['name']
         brand = item['brand']
         qty = str(item['quantity'])
         cost_price = "Rs. " + str(item['cost_price'])
         subtotal = "Rs. " + str(item['subtotal'])

         name_space = " " * (24 - len(name)) if len(name) < 24 else ""
         brand_space = " " * (20 - len(brand)) if len(brand) < 20 else ""
         qty_space = " " * (6 - len(qty)) if len(qty) < 6 else ""
         cp_space = " " * (12 - len(cost_price)) if len(cost_price) < 12 else ""
         sub_space = " " * (10 - len(subtotal)) if len(subtotal) < 10 else ""

         print(name + name_space + brand + brand_space + qty_space + qty + " | " + cp_space + cost_price + " | " + sub_space + subtotal)

         print("-" * 75)
         print("Total Cost: Rs. " + str(total_cost))
         print("VAT (13%): Rs."+str(vat))
         print("Grand Total: Rs."+str(grand_total))
         print("-" * 75)

         invoice_file = save_restock_invoice(supplier_name, restock_items, total_cost)
         write_products_to_file("products.txt", products)

         print("\nRestock completed successfully!")
         print("Invoice saved as: " + invoice_file)
    else:
         print("No items were restocked.")