import pytest
import source.myFunctions as myFunctions
import time


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


@pytest.mark.slow
def test_very_slow():
    time.sleep(2)
    result = myFunctions.divide(10, 5)
    assert result == 2


@pytest.mark.skip(reason="Out of scope....")
def test_add_multi():
    result = myFunctions.divide(10, 5)
    assert result == 2


@pytest.mark.xfail(reason="Maybe div zero....")
def test_add_mega():
    result = myFunctions.divide(1, 0)
    assert result == 2
