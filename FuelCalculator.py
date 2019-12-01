import math


class FuelCalculator:
    @staticmethod
    def calculate(mass):
        fuelNeeded = math.floor(int(mass) / 3) - 2
        if fuelNeeded <= 0:
            return 0
        return fuelNeeded + FuelCalculator.calculate(fuelNeeded)

