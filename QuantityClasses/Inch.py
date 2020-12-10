from QuantityMeaurementServices.LengthConversionOrCopmarision import LengthUtility


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
