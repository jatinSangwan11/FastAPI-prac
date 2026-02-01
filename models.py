from pydantic import BaseModel

class Product(BaseModel):
    """ this is the Product model """
    id: int
    name: str
    description: str
    price: float
    quantity: int

    # since we imported the BaseModel from pydantic for data validation we do not need to 
    # have this contructor
    
    # def __init__(self, id: int, name: str, description: str, price: float, quantity: int):
    #     self.id = id
    #     self.name = name
    #     self.description = description
    #     self.price = price
    #     self.quantity = quantity


        