import pytest
from Feet import Feet


def test_TwoFeetClassObjectsofEqualValue_WhenCheckedForEquality_ShouldReturnTrue():
    length1 = Feet(0.0)
    length2 = Feet(0.0)
    assert (length1 == length2) == True
