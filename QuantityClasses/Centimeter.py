from QuantityMeaurementServices.LengthConversionOrCopmarision import LengthUtility



class Centimeter:

    def __init__(self, inch):
        self.centimeter_value = float(inch)

    def __eq__(self, other):
        if other is None:
            return False
        else:
            return LengthUtility.check_equality(self, other)

    def __str__(self):
        return str(self.centimeter_value) + " centimeter"
