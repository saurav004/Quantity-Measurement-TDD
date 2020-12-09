class Feet:

    def __init__(self, feet):
        self.feet_value = float(feet)

    def __eq__(self, other):
        from QuantityClasses.Inch import Inch
        if other is None:
            return False
        elif isinstance(other, Feet):
            return self.feet_value == other.feet_value
        elif isinstance(other, Inch):
            return self.feet_value == other.inch_value/12
        else:
            raise TypeError

    def __str__(self):
        return str(self.feet_value) + " Feet"
