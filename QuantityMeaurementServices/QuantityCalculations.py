import enum


class QuantityCalculator:

    def __init__(self, unit, value):
        self.__value = value
        self.__unit = unit

    def __eq__(self, other):
        if isinstance(other, QuantityCalculator) and isinstance(self.__unit, QuantityEnum) and isinstance(other.__unit,
                                                                                                          QuantityEnum):
            if self.__unit.measureOf == other.__unit.measureOf:
                return self.__unit.convert_to_inch(self.__value) == other.__unit.convert_to_inch(other.__value)
        return False

    def __add__(self, other):
        if self.__unit.measureOf == other.__unit.measureOf:
            return QuantityCalculator(QuantityEnum.INCH, self.__unit.convert_to_inch(self.__value)
                                      + other.__unit.convert_to_inch(other.__value))


class QuantityEnum(enum.Enum):
    FEET = (12, "length")
    INCH = (1, "length")
    YARD = (36, "length")
    CENTIMETER = (0.4, "length")
    GALLON = (3780, "volume")
    LITER = (1000, "volume")
    MILLILITER = (1, "volume")

    def __init__(self, unit, measure_of):
        self.unit = unit
        self.measureOf = measure_of

    def convert_to_inch(self, value):
        return self.unit * value
