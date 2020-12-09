from QuantityClasses.Feet import Feet


class Inch:

    def __init__(self, inch):
        self.inch_value = float(inch)

    def __eq__(self, other):
        if other is None:
            return False
        elif isinstance(other, Inch):
            return self.inch_value == other.inch_value
        elif isinstance(other, Feet):
            return self.inch_value == other.feet_value*12
        else:
            raise TypeError

    def __str__(self):
        return str(self.inch_value) + " Inch"
