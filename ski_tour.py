from tour import Tour


class SkiTour(Tour):

    def __init__(self, name, price, description, resort):
        super().__init__(name, price, description)
        self.resort = resort

    def _get_specifics(self):
        return f"Ski resort: {self.resort}"