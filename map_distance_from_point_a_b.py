from math import radians, sin, cos, acos
from typing import Union


class Point:
    def __init__(self, latitude: float, longitude: float) -> None:
        self.latitude = radians(latitude)
        self.longitude = radians(longitude)

    def distance(self, other) -> float:
        cos_d = (
                sin(self.latitude) * sin(other.latitude) +
                cos(self.latitude) * cos(other.latitude) *
                cos(self.longitude - other.longitude))
        return 6371 * acos(cos_d)


class City(Point):
    def __init__(
            self,
            latitude: float,
            longitude: float,
            name: str,
            population: int) -> None:

        super().__init__(latitude, longitude)
        self.name = name
        self.population = population

    def show(self) -> None:
        print(f'Город {self.name}, население {self.population} чел.')


class Mountain(Point):
    def __init__(
            self,
            latitude: float,
            longitude: float,
            name: str,
            height: int) -> None:

        super().__init__(latitude, longitude)
        self.name = name
        self.height = height

    def show(self) -> None:
        print(f'Высота горы {self.name} - {self.height} м.')


def print_how_far(
        geo_object_1: Union[City, Mountain],
        geo_object_2: Union[City, Mountain]) -> None:

    print(
        f'От точки «{geo_object_1.name}» до точки «{geo_object_2.name}»'
        f' — {geo_object_1.distance(geo_object_2)} км.')


moscow = City(55.7522200, 37.6155600, 'Москва', 12615882)
everest = Mountain(27.98791, 86.92529, 'Эверест', 8848)
chelyabinsk = City(55.154, 61.4291, 'Челябинск', 1200703)

moscow.show()
everest.show()
print_how_far(moscow, everest)
print_how_far(moscow, chelyabinsk)
