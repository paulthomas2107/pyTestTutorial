import pytest
import source.shapes as shapes


@pytest.mark.parametrize("side_length, expected_area, random", [(5, 25, 12), (4, 16, 78), (9, 81, 987), (5, 25, 112)])
def test_multiple_square_areas(side_length, expected_area, random):
    assert random > side_length
    assert shapes.Square(side_length).area() == expected_area


@pytest.mark.parametrize("side_length, expected_perimeter", [(3, 12), (4, 16), (5, 20)])
def test_multiple_perimeters(side_length, expected_perimeter):
    assert shapes.Square(side_length).perimeter() == expected_perimeter