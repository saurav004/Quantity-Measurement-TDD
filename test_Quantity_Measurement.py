import pytest
from Feet import Feet
from Inch import Inch
from Yard import Yard


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


@pytest.mark.parametrize("length1, length2", [
    (feet_object, feet_object),
    (yard_object, yard_object),
    (inch_object, inch_object)])
def test_GivenTwoReferenceOfSameClassObject_WhenCheckedForEquality_ShouldReturnTrue(length1, length2):
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
