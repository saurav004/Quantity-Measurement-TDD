import pytest
from Feet import Feet


def test_GivenTwoFeetClassObjectsOfEqualValue_WhenCheckedForEquality_ShouldReturnTrue():
    length1 = Feet(0.0)
    length2 = Feet(0.0)
    assert (length1 == length2) == True


def test_GivenTwoReferenceOfSameFeetObject_WhenCheckedForEquality_ShouldReturnTrue():
    length1 = Feet(0.0)
    length2 = length1
    assert (length1 == length2) == True


def test_givenOnefloatValueOneFeetObjectOfSameValues_WhenFeetvalueCheckedforEquality_ShouldThrowException():
    length1 = Feet(0.0)
    length2 = float(0.0)
    with pytest.raises(TypeError):
        length1 == length2


def test_givenOneFeetObject_WhenCheckedIfNone_ShouldReturnFalse():
    length1 = Feet(0.0)
    assert (length1 == None) == False


def test_givenTwoFeetObjectsOfDifferentValues_WhenCHeckedForEquality_ShouldReturnFalse():
    length1 = Feet(0.0)
    length2 = Feet(0.2)
    assert (length1 == length2) == False
