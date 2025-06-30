import datetime
#function to load product data from file
def load_products_from_file(filename="products.txt"):
    """
    load the product data from a text file and calculate the selling price

    Parameters:
    filename(str): The name of the file to read from the "products.txt".

    Returns:
    List: A list of products where each product is represented as a list containing:
        [product name, brand, stock, selling price(as string), country]

    """
    products = []
    file = open(filename, 'r')
    lines = file.readlines()
    file.close()

    for line in lines:
        parts = line.split(', ')
        cost_price = int(parts[3])
        selling_price = cost_price * 2
        country = parts[4].replace('\n', '').replace('\r', '')  # Remove newline

        product = [
            parts[0],
            parts[1],
            parts[2],
            str(selling_price),
            country
        ]
        products.append(product)
    return products