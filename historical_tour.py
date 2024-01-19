from tour import Tour


class HistoricalTour(Tour):

    def __init__(self, name, price, description, period):
        super().__init__(name, price, description)
        self.period = period

    def _get_specifics(self):
        return f"Historical period: {self.period}"