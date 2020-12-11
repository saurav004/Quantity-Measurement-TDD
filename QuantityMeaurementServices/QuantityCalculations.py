import enum


class QuantityCalculator:

    def __init__(self, unit, value):
        self.__value = value
        self.__unit = unit

    def __eq__(self, other):
        if isinstance(other, QuantityCalculator) and isinstance(self.__unit, QuantityEnum) and isinstance(other.__unit, QuantityEnum):
            return self.__unit.convert_to_inch(self.__value) == other.__unit.convert_to_inch(other.__value)
        else:
            return False


class QuantityEnum(enum.Enum):
    FEET = 12
    INCH = 1
    YARD = 36
    CENTIMETER = 0.4

    def __init__(self, unit):
        self.unit = unit

    def convert_to_inch(self, value):
        return self.unit * value
