from QuantityMeaurementServices.LengthConversionOrCopmarision import LengthUtility
from QuantityClasses.Feet import Feet
from QuantityClasses.Yard import Yard


class Inch:

    def __init__(self, inch):
        self.inch_value = float(inch)

    def __eq__(self, other):
        if other is None:
            return False
        else:
            return LengthUtility.check_equality(self, other)

    def __str__(self):
        return str(self.inch_value) + " Inch"
