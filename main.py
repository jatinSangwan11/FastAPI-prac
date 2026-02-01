from math import prod
from fastapi import FastAPI
from models import Product

app = FastAPI()

# here the web server return html/JSON
# when we send the data from the server to the web it should be in 
# the proper format there comes REST API
@app.get("/")
def read_root():   # here I don't have to mention async(already in async)
    return {"message": "Hello FastAPI"}


products = [
    # Product(1,"phone","this is an iphone", 12444.5, 1) instead of this when using pydantic
    # pass like below :::::
    Product(id=1, name="Laptop", description="14-inch ultrabook with SSD storage", price=74999.99, quantity=5),
    Product(id=2, name="Smartphone", description="5G-enabled smartphone with AMOLED display", price=32999.50, quantity=12),
    Product(id=3, name="Wireless Mouse", description="Ergonomic wireless mouse with USB receiver", price=899.00, quantity=40),
    Product(id=4, name="Mechanical Keyboard", description="Backlit mechanical keyboard with blue switches", price=3499.99, quantity=18),
    Product(id=5, name="Headphones", description="Noise-cancelling over-ear headphones", price=5999.00, quantity=10),
    Product(id=6, name="Monitor", description="24-inch full HD LED monitor", price=12999.75, quantity=7),
    Product(id=7, name="External Hard Drive", description="1TB USB 3.0 external hard drive", price=4499.50, quantity=15),
    Product(id=8, name="USB-C Hub", description="Multi-port USB-C hub with HDMI support", price=1999.00, quantity=25),
    Product(id=9, name="Webcam", description="1080p HD webcam with built-in microphone", price=2799.99, quantity=14),
    Product(id=10, name="Desk Lamp", description="LED desk lamp with adjustable brightness", price=1499.00, quantity=30)

]

@app.get("/products")
def get_all_products():
    return products


@app.get("/product/{id}")
def get_product_by_id(id: int):
    """ Need to add data validation as it might be possible that product is missing """
    for product in products:
        if(product.id == id):
            return product
    return f"there is not product with the {id}"

# add product

@app.post("/product")
def add_product(product: Product):
    products.append(product)
    return product

@app.put("/products/{product_id}")
def update_product(product_id: int, product: Product):
    for i in range(len(products)):
        if products[i].id == product_id:
            products[i] = product
            return {"message": "Product updated successfully", "product": product}
    return {"error": "Product not found"}

@app.delete("/products/{product_id}")
def delete_product(product_id: int):
    for i in range(len(products)):
        if products[i].id == product_id:
            del products[i]
            return {"message": "Product deleted successfully"}
    return {"error": "Product not found"}