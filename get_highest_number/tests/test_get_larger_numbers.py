#test_get_larger_numbers
import pytest
from get_highest_number.answer import get_larger_numbers1

def test_pick_from_different_arrays():
    assert get_larger_numbers1.get_larger_numbers([13, 64, 15, 17, 88], [23, 14, 53, 17, 80]) == [23, 64, 53, 17, 88]

def test_pick_small_arrays():
    assert get_larger_numbers1.get_larger_numbers([], []) == []

def test_pick_when_same():
    assert get_larger_numbers1.get_larger_numbers([10, 20, 30], [10, 20, 30]) == [10, 20, 30]

def test_raises_exception():
    with pytest.raises(IndexError):
        get_larger_numbers1.get_larger_numbers([10, 20, 30], [10, 20])

def test_one_not_list_of_numbers():
    with pytest.raises(TypeError):
        get_larger_numbers1.get_larger_numbers('a', [10])