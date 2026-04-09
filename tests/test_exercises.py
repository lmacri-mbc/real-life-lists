# tests/test_lists.py
import exercises

def test_create_list():
    assert exercises.create_list() == [1, 2, 3, 4, 5]


def test_add_ten():
    assert exercises.add_ten([1, 2, 3]) == [1, 2, 3, 10]


def test_second_element():
    assert exercises.second_element([1, 9, 3]) == 9


def test_change_last_to_twenty():
    assert exercises.change_last_to_twenty([1, 2, 3]) == [1, 2, 20]


def test_remove_three():
    assert exercises.remove_three([1, 2, 3, 4]) == [1, 2, 4]


def test_pop_first():
    popped, new_list = exercises.pop_first([5, 6, 7])
    assert popped == 5
    assert new_list == [6, 7]


def test_list_length():
    assert exercises.list_length([10, 20, 30]) == 3


def test_concatenate_lists():
    assert exercises.concatenate_lists([1, 2]) == [1, 2, 6, 7, 8]


def test_contains_five():
    assert exercises.contains_five([1, 5, 9]) is True
    assert exercises.contains_five([1, 2, 3]) is False


def test_reverse_list():
    assert exercises.reverse_list([1, 2, 3]) == [3, 2, 1]


def test_sort_descending():
    assert exercises.sort_descending([3, 1, 2]) == [3, 2, 1]


def test_remove_duplicates():
    assert exercises.remove_duplicates([2, 2, 3, 3, 4]) == [2, 3, 4]
  
