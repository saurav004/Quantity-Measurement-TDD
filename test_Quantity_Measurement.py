import pytest
from Feet import Feet


def test_GivenTwoFeetClassObjectsOfEqualValue_WhenCheckedForEquality_ShouldReturnTrue():
    length1 = Feet(0.0)
    length2 = Feet(0.0)
    assert (length1 == length2) == True


def test_GivenTwoReferenceOfSameFeetObject_WhenCheckedForEquality_ShouldReturTrue():
    length1 = Feet(0.0)
    length2 = length1
    assert (length1 == length2) == True

def test_givenOnefloatValueOneFeetObjectOfSameValues_WhenFeetvalueCheckedforEquality_ShouldThrowException():
    length1 = Feet(0.0)
    length2 = float(0.0)
    with pytest.raises(TypeError):
        length1 == length2

