import pytest
import source.myFunctions as myFunctions


def test_add():
    result = myFunctions.add(1, 4)
    assert result == 5