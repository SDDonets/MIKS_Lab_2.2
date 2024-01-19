from prototype import Prototype


class TourPackage(Prototype):

    def __init__(self, name, tours):
        self.name = name
        self.tours = tours

    def __str__(self):
        return f"{self.name} with {len(self.tours)} tours"

    def _get_package_details(self):
        details = []
        for tour in self.tours:
            details.append(str(tour))
        return "\n".join(details)