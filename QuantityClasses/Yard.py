

class Yard:

    def __init__(self, yard):
        self.yard_value = yard

    def __eq__(self, other):
        from QuantityClasses.Feet import Feet
        from QuantityClasses.Inch import Inch
        if other is None:
            return False
        elif isinstance(other, Yard):
            return self.yard_value == other.yard_value
        elif isinstance(other, Feet):
            return self.yard_value == other.feet_value/3
        elif isinstance(other, Inch):
            return self.yard_value == other.inch_value/36
        else:
            raise TypeError

    def __str__(self):
        return str(self.yard_value) + " Yard"
