from QuantityMeaurementServices.LengthConversionOrCopmarision import LengthUtility


class Feet:

    def __init__(self, feet):
        self.feet_value = float(feet)

    def __eq__(self, other):
        if other is None:
            return False
        else:
            return LengthUtility.check_equality(self, other)

    def __str__(self):
        return str(self.feet_value) + " Feet"
