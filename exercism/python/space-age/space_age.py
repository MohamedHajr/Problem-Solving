plants_years = {
    'mercury':  0.2408467,
    'venus':  0.61519726,
    'mars': 1.8808158,
    'jupiter': 11.862615,
    'saturn': 29.447498,
    'uranus': 84.016846,
    'neptune': 164.79132,
    'earth': 1
}


class SpaceAge(object):
    def __init__(self, seconds):
        self.seconds = seconds
        for planet in plants_years:
            self.add_function(planet)

    def add_function(self, planet):
        setattr(self, 'on_' + planet,
                lambda: self.calculate_years(planet))

    def calculate_years(self, planet):
        return round(self.seconds / 31557600 / plants_years[planet], 2)
