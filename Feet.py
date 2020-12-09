class Feet:

    def __init__(self, feet):
        self.feet_value = float(feet)

    def __eq__(self, other):
        if  other == None:
            return False
        elif isinstance(other, Feet):
            return self.feet_value == other.feet_value
        else:
            raise TypeError

    def __str__(self):
        return str(self.feet_value) + " Feet"
