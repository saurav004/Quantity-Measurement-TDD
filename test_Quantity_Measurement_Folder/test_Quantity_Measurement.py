from copy import copy

import pytest

from QualityMeaurementServices.LengthConversionOrCopmarision import LengthUtility
from QuantityClasses.Centimeter import Centimeter
from QuantityClasses.Feet import Feet
from QuantityClasses.Inch import Inch
from QuantityClasses.Yard import Yard


@pytest.fixture
def feet_object():
    return Feet(0.0)


@pytest.fixture
def yard_object():
    return Yard(0.0)


@pytest.fixture()
def inch_object():
    return Inch(0.0)


@pytest.mark.parametrize("length1, length2", [
    (feet_object, feet_object),
    (yard_object, yard_object),
    (inch_object, inch_object)])
def test_GivenTwoObjectsOfSameClassAndValue_WhenCheckedForEquality_ShouldReturnTrue(length1, length2):
    assert (length1 == length2)


def test_GivenTwoReferenceOfSameClassObject_WhenCheckedForEquality_ShouldReturnTrue():
    length1 = Feet(1.0)
    length2 = length1
    assert (length1 == length2)


def test_givenOnefloatValueOneFeetObjectOfSameValues_WhenFeetvalueCheckedforEquality_ShouldThrowException():
    length1 = Feet(0.0)
    length2 = float(0.0)
    with pytest.raises(TypeError):
        length1 == length2


@pytest.mark.parametrize("length1", [
    feet_object,
    yard_object,
    inch_object])
def test_givenOneObject_WhenCheckedIfNone_ShouldReturnFalse(length1):
    assert (length1 == None) == False


def test_givenTwoFeetObjectsOfDifferentValues_WhenCheckedForEquality_ShouldReturnFalse():
    length1 = Feet(0.0)
    length2 = Feet(0.2)
    assert (length1 == length2) == False


def test_givenTwoYardObjectsOfDifferentValues_WhenCheckedForEquality_ShouldReturnFalse():
    length1 = Yard(0.0)
    length2 = Yard(0.2)
    assert (length1 == length2) == False


def test_givenTwoInchObjectsOfDifferentValues_WhenCheckedForEquality_ShouldReturnFalse():
    length1 = Inch(0.0)
    length2 = Inch(0.2)
    assert (length1 == length2) == False


def test_givenOnefloatValueOneYardObjectOfSameValues_WhenFeetvalueCheckedforEquality_ShouldThrowException():
    length1 = Yard(0.0)
    length2 = float(0.0)
    with pytest.raises(TypeError):
        length1 == length2


def test_givenOnefloatValueOneInchObjectOfSameValues_WhenFeetvalueCheckedforEquality_ShouldThrowException():
    length1 = Inch(0.0)
    length2 = float(0.0)
    with pytest.raises(TypeError):
        length1 == length2


def test_givenOneInchObjectandOneFeetObject_WhenCompared_ShouldreturnExpected():
    length1 = Feet(1.0)
    length2 = Inch(12.0)
    assert length2 == length1


def test_givenOneFeetObjectandOneYardObject_WhenCompared_ShouldreturnExpected():
    length1 = Feet(3.0)
    length2 = Yard(1.0)
    assert length2 == length1


def test_givenOneInchObjectandOneYardObject_WhenCompared_ShouldReturnExpectedOutput():
    length1 = Inch(1.0)
    length2 = Yard(1.0)
    assert length1 != length2


def test_givenOneFeetObjectandOneYardObject_WhenCompared_ShouldreturnFalseHere():
    length1 = Feet(1.0)
    length2 = Yard(1.0)
    assert length1 != length2


def test_givenOneYard36Inch_WhenCompared_ShouldReturnTrue():
    length1 = Yard(1.0)
    length2 = Inch(36.0)
    assert length1 == length2

def test_given36InchOneYard_WhenCompared_ShouldReturnTrue():
    length1 = Yard(1.0)
    length2 = Inch(36.0)
    assert length2 == length1

def test_given1Yard3Feet_WhenCompared_ShouldReturnTrue():
    length1 = Yard(1.0)
    length2 = Feet(3.0)
    assert length2 == length1


def test_Given2InchAnd5Cm_WhenComparedForEquality_ShouldReturnFalse():
    length1 = Inch(2)
    length2 = Centimeter(5)
    assert length1 != length2

def test_GivenTwoInchObjectsOfValue2Inch_WhenAdded_ShouldGiveExpectedValue():
    length1 = Inch(2.0)
    length2 = Inch(2.0)
    assert Inch(LengthUtility.add(length1, length2)) == Inch(4.0)
