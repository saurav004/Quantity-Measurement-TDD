class Feet:

    def __init__(self, feet):
        self.feet = float(feet)

    def __eq__(self, other):
        return self.feet == other.feet
