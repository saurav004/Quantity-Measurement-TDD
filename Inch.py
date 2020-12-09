class Inch:

    def __init__(self, inch):
        self.inch_value = float(inch)

    def __eq__(self, other):
        if  other == None:
            return False
        elif isinstance(other, Inch):
            return self.inch_value == other.inch_value
        else:
            raise TypeError

    def __str__(self):
        return str(self.inch_value) + " Inch"
