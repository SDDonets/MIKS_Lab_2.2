from tour import Tour


class BeachTour(Tour):

    def __init__(self, name, price, description):
        super().__init__(name, price, description)

    def _get_specifics(self):
        return "Includes sunbeds and umbrellas"