import datetime
#function to write product to file
def write_products_to_file(filename, products):
    """
    Writes the updated product list back to the text file

    Parameters:
    filename(str): The name of the file to write to.
    products(list): A list of product data, where each product is a list containing product name, brand, quantity, selling price, and country.

    Stores the cost price (half of the selling price) in the file.
    """
    file = open(filename, 'w')
    for p in products:
        cost_price = int(p[3]) // 2
        line = p[0] + ", " + p[1] + ", " + p[2] + ", " + str(cost_price) + ", " + p[4] + "\n"
        file.write(line)
    file.close()

#funtion to generate invoice filename
def generate_invoice_filename(prefix, customer_name):
    """
    Generates a unique filename for invoice using a timestamp.

    Parameters:
        prefix(str): A prefix string to identify the type of invoice.
        customer_name(str): The name of the customer or supplier.

    Returns:
        str: A formatted filename including the prefix, customer/supplier name, and timestamp.
    """
    now = datetime.datetime.now()
    timestamp = (str(now.year) + str(now.month) + str(now.day) + "_" + str(now.hour)+ str(now.minute) + str(now.second))
    return prefix + customer_name.replace(" ", "_") + "_" + timestamp + ".txt"

#funtion to save sale invoice
def save_sale_invoice(customer_name, bought_items, total, total_free_items):
    """
    Saves a sale invoice to a text file.

    Parameters:
        customer_name(str): The name of the customer that makes the purchase.
        bought_items(list): A list of dictionaries with keys: 'name', 'quantity', and 'price'.
        total(int): The total purchase amount.
        total_free_items(int): The number of free items given as an offer.

    Returns:
        str: The filename of the saved invoice.
    """
    filename= generate_invoice_filename("sale",customer_name)
    now = datetime.datetime.now()
    timestamp = str(now.year) + "-" + str(now.month) + "-" + str(now.day) + "-" + str(now.hour) + "-" + str(now.minute) + "-" + str(now.second)
    filename = "invoice_" + customer_name.replace(" ", "") + "-" + timestamp + ".txt"

    w = open(filename, 'w')
    w.write("\n" * 2)
    w.write("\t" * 7 + "WeCare Store\n\n")
    w.write("\t" * 5 + "Newroad, Kathmandu | Phone No: 9813844416\n\n")
    w.write("-" * 75 + "\n")
    w.write("\t" * 4 + "Customer Invoice\n")
    w.write("-" * 75 + "\n\n")
    w.write("Customer Name: " + customer_name + "\n")
    w.write("Date/Time: " + str(now.year) + "-" + str(now.month) + "-" + str(now.day) + " " + str(now.hour) + ":" + str(now.minute) + ":" + str(now.second) + "\n")
    w.write("-" * 75 + "\n\n")
    
    #Write purchased items
    w.write("Purchased Products:\n")
    for item in bought_items:
        line = item['name'] + ": " + str(item['quantity']) + " x " + str(item['price']) + " = " + str(item['quantity'] * int(item['price'])) + "\n"
        w.write(line)
    w.write("-" * 75 + "\n")
    w.write("TOTAL: " + str(total) + "\n")
    w.write("-" * 75 + "\n")

    if total_free_items:
        w.write("\n")
        w.write("\nYou have got " + str(total_free_items) + " free items from products\n\n")
        w.write("-" * 75 + "\n")
        w.write("Thank you for shopping with us!\n")
        w.write("-" * 75 + "\n")
        w.close()
    return filename

#function to save restock invoice
def save_restock_invoice(supplier_name, restock_items, total_cost):
    """
    Saves a restock invoice to a text file.

    Parameters:
        supplier_name(str): Name of the supplier.
        restock_items(list): A list of dictionaries with the restocked item details including:'name', 'brand', 'quantity', 'cost_price', and 'subtotal'.
        total_cost(int): Total restocking cost before VAT.

    Returns:
        str: The filename of the saved invoice.
    """
    filename = generate_invoice_filename("restock", supplier_name)
    now = datetime.datetime.now()

    vat = int(total_cost*13/100)
    grand_total = total_cost +vat

    w = open(filename, 'w')
    w.write("\n" * 2)
    w.write("\t" * 7 + "WeCare Store\n\n")
    w.write("\t" * 5 + "Newroad, Kathmandu | Phone No: 9813844416\n\n")
    w.write("-" * 75 + "\n")
    w.write("\t" * 4 + "Restock Invoice\n")
    w.write("-" * 75 + "\n\n")
    w.write("Supplier Name: " + supplier_name + "\n")
    w.write("Date/Time: " + str(now.year) + "-" + str(now.month) + "-" + str(now.day) + " " + str(now.hour) + ":" + str(now.minute) + ":" + str(now.second) + "\n")
    w.write("-" * 75 + "\n\n")
    w.write("Restocked Products:\n")

    for item in restock_items:
        w.write("Product: " + item['name'] + "\n")
        w.write("Brand: " + item['brand'] + "\n")
        w.write("Quantity: " + str(item['quantity']) + "\n")
        w.write("Cost Price: Rs. " + str(item['cost_price']) + "\n")
        w.write("Subtotal: Rs. " + str(item['subtotal']) + "\n")
        w.write("-" * 50 + "\n")

    w.write("-" * 75 + "\n")
    w.write("TOTAL COST: Rs. " + str(total_cost) + "\n")
    w.write("VAT (13%):  Rs. " + str(vat) + "\n")
    w.write("Grand Total: Rs. " + str(grand_total) + "\n")
    w.write("-" * 75 + "\n")
    w.write("Inventory updated successfully\n")
    w.write("-" * 75 + "\n")
    w.close()

    return filename