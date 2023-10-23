import pytest
import source.myFunctions as myFunctions


def test_add():
    result = myFunctions.add(1, 4)
    assert result == 5


def test_add_strings():
    result = myFunctions.add("I like ", "Burgers")
    assert result == "I like Burgers"


def test_divide():
    result = myFunctions.divide(10, 5)
    assert result == 2


def test_divide_by_zero():
    with pytest.raises(ValueError):
        myFunctions.divide(10, 0)
