from prototype import Prototype
from tour import Tour
from beach_tour import BeachTour
from cruise_tour import CruiseTour
from historical_tour import HistoricalTour
from ski_tour import SkiTour
from festival_tour import FestivalTour
from tour_package import TourPackage

# We create tour prototypes

prototype = Prototype()

beach_tour = BeachTour("Vacation on the beach", 500, "7 days on the coast")
prototype.register_object('beach', beach_tour)

cruise_tour = CruiseTour("Caribbean Cruise", 1200, "7 days on Caribbean sea", "Royal Caribbean")
prototype.register_object('cruise', cruise_tour)

historical_tour = HistoricalTour("Ancient Rome", 850, "3 days in Rome", "Antiquity")
prototype.register_object('historical', historical_tour)

ski_tour = SkiTour("Austrian Alps", 1200, "7 days of skiing", "Kitzbühel")
prototype.register_object('ski', ski_tour)

festival_tour = FestivalTour("Oktoberfest", 990, "Visiting legendary festival", "Oktoberfest")
prototype.register_object('festival', festival_tour)

# We create tour packages

summer_tours = TourPackage("Summer Tours", [
    prototype.clone('beach'),
    prototype.clone('cruise')
])

winter_tours = TourPackage("Winter Tours", [
    prototype.clone('ski'),
    prototype.clone('festival')
])

print(summer_tours)
print(winter_tours)

# We display package details
print(summer_tours._get_package_details())
print(winter_tours._get_package_details())