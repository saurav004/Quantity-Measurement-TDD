


class LengthUtility:

    @classmethod
    def convert_to_inch(cls, obj):
        from QuantityClasses.Feet import Feet
        from QuantityClasses.Inch import Inch
        from QuantityClasses.Yard import Yard
        from QuantityClasses.Centimeter import Centimeter
        if isinstance(obj, Feet):
            return obj.feet_value * 12
        elif isinstance(obj, Inch):
            return obj.inch_value
        elif isinstance(obj, Yard):
            return obj.yard_value * 36
        elif isinstance(obj, Centimeter):
            return obj.centimeter_value / 2.54
        else:
            raise TypeError

    @classmethod
    def check_equality(cls, obj1, obj2):
        return cls.convert_to_inch(obj1) == cls.convert_to_inch(obj2)
