import pytest


def test_area(myRectangle):
    assert myRectangle.area() == 10 * 20


def test_perimeter(myRectangle):
    assert myRectangle.perimeter() == (10 * 2) + (20 * 2)


def test_not_equal(myRectangle, weird_rectangle):
    assert myRectangle != weird_rectangle
