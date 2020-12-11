import enum


class QuantityCalculator:

    def __init__(self, unit, value):
        self.__value = value
        self.__unit = unit

    def __eq__(self, other):
        if isinstance(other, QuantityCalculator) and isinstance(self.__unit, QuantityEnum) and isinstance(other.__unit,
                                                                                                          QuantityEnum):
            if self.__unit.measureOf == other.__unit.measureOf:
                return self.__unit.convert_to_base_unit(self.__value) == other.__unit.convert_to_base_unit(other.__value)
        return False

    def __add__(self, other):
        base_of_measurement = {
            "volume": QuantityEnum.MILLILITER,
            "length": QuantityEnum.INCH,
            "weight": QuantityEnum.KILOGRAM,
            "temperature": QuantityEnum.CELSIUS
        }
        if self.__unit.measureOf == other.__unit.measureOf:
            return QuantityCalculator(base_of_measurement[self.__unit.measureOf],
                                      self.__unit.convert_to_base_unit(self.__value)
                                      + other.__unit.convert_to_base_unit(other.__value))


class QuantityEnum(enum.Enum):
    FEET = (12, "length")
    INCH = (1, "length")
    YARD = (36, "length")
    CENTIMETER = (0.4, "length")
    GALLON = (3780, "volume")
    LITER = (1000, "volume")
    MILLILITER = (1, "volume")
    TONNE = (1000, "weight")
    GRAM = (0.001, "weight")
    KILOGRAM = (1, "weight")
    CELSIUS = (1, "temperature")
    FAHRENHEIT = (0.5555, "temperature", True)

    def __init__(self, unit, measure_of, is_fahrenheit=False):
        self.is_fahrenheit = is_fahrenheit
        self.unit = unit
        self.measureOf = measure_of

    def convert_to_base_unit(self, value):
        if self.is_fahrenheit:
            return round((value - 32) * self.unit)
        return self.unit * value
