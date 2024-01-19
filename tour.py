from prototype import Prototype


class Tour(Prototype):

    def __init__(self, name, price, description):
        self.name = name
        self.price = price
        self.description = description

    def __str__(self):
        return f"{self.name} ({self.price})"