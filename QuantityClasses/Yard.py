class Yard:

    def __init__(self, yard):
        self.yard_value = yard

    def __eq__(self, other):
        if other is None:
            return False
        elif isinstance(other, Yard):
            return self.yard_value == other.yard_value
        else:
            raise TypeError

    def __str__(self):
        return str(self.yard_value) + " Yard"
