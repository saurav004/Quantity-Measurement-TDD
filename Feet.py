class Feet:

    def __init__(self, feet):
        self.feet_value = float(feet)

    def __eq__(self, other):
        if isinstance(other, Feet):
            return self.feet_value == other.feet_value
        else:
            raise TypeError
