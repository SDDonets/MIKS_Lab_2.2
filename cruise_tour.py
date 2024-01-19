from tour import Tour


class CruiseTour(Tour):

    def __init__(self, name, price, description, ship_name):
        super().__init__(name, price, description)
        self.ship_name = ship_name

    def _get_specifics(self):
        return f"Cruise ship: {self.ship_name}"