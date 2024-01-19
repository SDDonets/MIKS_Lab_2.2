from tour import Tour


class FestivalTour(Tour):

    def __init__(self, name, price, description, festival):
        super().__init__(name, price, description)
        self.festival = festival

    def _get_specifics(self):
        return f"Festival: {self.festival}"