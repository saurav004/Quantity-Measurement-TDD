from QualityMeaurementServices.LengthConversionOrCopmarision import LengthUtility


class Yard:

    def __init__(self, yard):
        self.yard_value = yard

    def __eq__(self, other):
        if other is None:
            return False
        else:
            return LengthUtility.check_equality(self, other)

    def __str__(self):
        return str(self.yard_value) + " Yard"
