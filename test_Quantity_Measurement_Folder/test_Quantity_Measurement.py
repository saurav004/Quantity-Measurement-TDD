import pytest

from QuantityMeaurementServices.QuantityCalculations import QuantityCalculator, QuantityEnum


@pytest.fixture
def feet_object():
    return QuantityCalculator(QuantityEnum.FEET, 1.0)


@pytest.fixture
def yard_object():
    return QuantityCalculator(QuantityEnum.INCH, 1.0)


@pytest.fixture()
def inch_object():
    return QuantityCalculator(QuantityEnum.YARD, 1.0)


@pytest.fixture()
def centimeter_object():
    return QuantityCalculator(QuantityEnum.CENTIMETER, 1.0)


@pytest.mark.parametrize("length1, length2", [
    (feet_object, feet_object),
    (inch_object, inch_object),
    (yard_object, yard_object),
    (centimeter_object, centimeter_object)])
def test_GivenTwoObjectsOfSameClassAndValue_WhenCheckedForEquality_ShouldReturnTrue(length1, length2):
    assert QuantityCalculator(QuantityEnum.FEET, 0.0) == QuantityCalculator(QuantityEnum.FEET, 0.0)


@pytest.mark.parametrize("length1", [
    feet_object,
    yard_object,
    inch_object,
    centimeter_object])
def test_GivenTwoReferenceOfSameObjectAndClass_WhenCheckedForEquality_ShouldReturnTrue(length1):
    length2 = length1
    assert length1 == length2


@pytest.mark.parametrize("length1", [
    feet_object,
    yard_object,
    inch_object,
    centimeter_object])
def test_givenOnefloatValueOneFeetObjectOfSameValues_WhenFeetvalueCheckedforEquality_ShouldReturnFalse(length1):
    length2 = float(1.0)
    assert length1 != length2


@pytest.mark.parametrize("length1", [
    feet_object,
    yard_object,
    inch_object,
    centimeter_object])
def test_givenOneObject_WhenCheckedIfNone_ShouldReturnFalse(length1):
    assert length1 is not None


def test_givenTwoFeetObjectsOfDifferentValues_WhenCheckedForEquality_ShouldReturnFalse():
    assert QuantityCalculator(QuantityEnum.FEET, 1.0) != QuantityCalculator(QuantityEnum.FEET, 2.0)


def test_givenTwoInchObjectsOfDifferentValues_WhenCheckedForEquality_ShouldReturnFalse():
    assert QuantityCalculator(QuantityEnum.INCH, 1.0) != QuantityCalculator(QuantityEnum.INCH, 2.0)


def test_givenTwoYardObjectsOfDifferentValues_WhenCheckedForEquality_ShouldReturnFalse():
    assert QuantityCalculator(QuantityEnum.YARD, 1.0) != QuantityCalculator(QuantityEnum.YARD, 2.0)


def test_givenTwoCentimeterObjectsOfDifferentValues_WhenCheckedForEquality_ShouldReturnFalse():
    assert QuantityCalculator(QuantityEnum.CENTIMETER, 1.0) != QuantityCalculator(QuantityEnum.CENTIMETER, 2.0)


def test_givenOneInchObjectandOneFeetObject_WhenCompared_ShouldreturnExpected():
    length1 = QuantityCalculator(QuantityEnum.FEET, 1.0)
    length2 = QuantityCalculator(QuantityEnum.INCH, 12.0)
    assert length2 == length1


def test_givenOneFeetObjectandOneYardObject_WhenCompared_ShouldreturnExpected():
    assert QuantityCalculator(QuantityEnum.FEET, 3.0) == QuantityCalculator(QuantityEnum.YARD, 1.0)


def test_givenOneFeetObjectandOneYardObject_WhenCompared_ShouldreturnFalseHere():
    assert QuantityCalculator(QuantityEnum.FEET, 1.0) != QuantityCalculator(QuantityEnum.YARD, 1.0)


def test_givenOneInchObjectandOneYardObject_WhenCompared_ShouldReturnExpectedOutput():
    assert QuantityCalculator(QuantityEnum.INCH, 1.0) != QuantityCalculator(QuantityEnum.YARD, 1.0)


def test_givenOneYard36Inch_WhenCompared_ShouldReturnTrue():
    assert QuantityCalculator(QuantityEnum.YARD, 1.0) == QuantityCalculator(QuantityEnum.INCH, 36.0)


def test_given36InchOneYard_WhenCompared_ShouldReturnTrue():
    assert QuantityCalculator(QuantityEnum.INCH, 36.0) == QuantityCalculator(QuantityEnum.YARD, 1.0)


def test_givenOneFeetObjectandOneYardObjectOfvalue1_WhenCompared_ShouldreturnExpected():
    assert QuantityCalculator(QuantityEnum.YARD, 1.0) == QuantityCalculator(QuantityEnum.FEET, 3.0)


def test_Given2InchAnd5Cm_WhenComparedForEquality_ShouldReturnFalse():
    assert QuantityCalculator(QuantityEnum.INCH, 2.0) == QuantityCalculator(QuantityEnum.CENTIMETER, 5.0)


def test_GivenTwoInchObjectsOfValue2Inch_WhenAdded_ShouldGiveExpectedValue():
    length1 = QuantityCalculator(QuantityEnum.INCH, 2.0)
    length2 = QuantityCalculator(QuantityEnum.INCH, 2.0)
    assert (length1 + length2) == QuantityCalculator(QuantityEnum.INCH, 4.0)


def test_GivenOneFeetAnd2Inch_WhenAdded_ShouldGiveExpectedValue():
    length1 = QuantityCalculator(QuantityEnum.FEET, 1.0)
    length2 = QuantityCalculator(QuantityEnum.INCH, 2.0)
    assert (length1 + length2) == QuantityCalculator(QuantityEnum.INCH, 14.0)


def test_GivenTwoFeetObjectsofValue1Each_WhenAdded_ShouldGiveExpectedValue():
    length1 = QuantityCalculator(QuantityEnum.FEET, 1.0)
    length2 = QuantityCalculator(QuantityEnum.FEET, 1.0)
    assert (length1 + length2) == QuantityCalculator(QuantityEnum.INCH, 24.0)


def test_Given2InchObjectand2andHalfcmObject_WhenAdded_ShouldGiveExpectedValue():
    length1 = QuantityCalculator(QuantityEnum.INCH, 2.0)
    length2 = QuantityCalculator(QuantityEnum.CENTIMETER, 2.5)
    assert (length1 + length2) == QuantityCalculator(QuantityEnum.INCH, 3.0)


@pytest.mark.parametrize("volume1, volume2", [
    (QuantityCalculator(QuantityEnum.GALLON, 1.0), QuantityCalculator(QuantityEnum.LITER, 3.78)),
    (QuantityCalculator(QuantityEnum.LITER, 1.0), QuantityCalculator(QuantityEnum.MILLILITER, 1000))])
def test_Given1GallonAnd3point78Litres_WhenCompared_ShouldGiveExpectedValue(volume1, volume2):
    assert volume1 == volume2


@pytest.mark.parametrize("volume1,volume2,expected", [
    (QuantityCalculator(QuantityEnum.GALLON, 1.0),
     QuantityCalculator(QuantityEnum.LITER, 3.78),
     QuantityCalculator(QuantityEnum.LITER, 7.56)),
    (QuantityCalculator(QuantityEnum.LITER, 1.0),
     QuantityCalculator(QuantityEnum.MILLILITER, 1000),
     QuantityCalculator(QuantityEnum.LITER, 2))])
def test_GivenTwoVolume_WhenAdded_ShouldReturnExpected(volume1, volume2, expected):
    assert volume1 + volume2 == expected


@pytest.mark.parametrize("weight1, weight2", [
    (QuantityCalculator(QuantityEnum.KILOGRAM, 1.0), QuantityCalculator(QuantityEnum.GRAM, 1000)),
    (QuantityCalculator(QuantityEnum.TONNE, 1.0), QuantityCalculator(QuantityEnum.KILOGRAM, 1000))])
def test_GivenTwoWieghtQuantities_WhenCompared_ShouldReturnExpectedBoolean(weight1, weight2):
    assert weight1 == weight2


@pytest.mark.parametrize("weight1,weight2,expected", [
    (QuantityCalculator(QuantityEnum.TONNE, 1.0),
     QuantityCalculator(QuantityEnum.GRAM, 1000),
     QuantityCalculator(QuantityEnum.KILOGRAM, 1001))])
def test_GivenTwoWieghtQuantities_WhenCompared_ShouldReturnExpected(weight1, weight2, expected):
    assert weight1 + weight2 == expected
