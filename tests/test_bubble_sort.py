from everyday_algorithms.sorts.bubble_sort import bubbleSort


def test_sort():
    assert bubbleSort([]) == []
    assert bubbleSort([1]) == [1]
    assert bubbleSort([1, 2]) == [1, 2]
    assert bubbleSort([2, 1]) == [1, 2]
    assert bubbleSort([1, 2, 3]) == [1, 2, 3]
    assert bubbleSort([3, 2, 1]) == [1, 2, 3]
    assert bubbleSort([1, 2, 3, 4]) == [1, 2, 3, 4]
    assert bubbleSort([4, 3, 2, 1]) == [1, 2, 3, 4]
    assert bubbleSort([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]
    assert bubbleSort([5, 4, 3, 2, 1]) == [1, 2, 3, 4, 5]

