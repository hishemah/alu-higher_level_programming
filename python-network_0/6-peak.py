#!/usr/bin/python3
"""Module that defines find_peak, which finds a peak in a list of integers."""


def find_peak(list_of_integers):
    """Return a peak of a list of unsorted integers, or None if it is empty.

    A peak is an element that is not smaller than its neighbours. Each step
    keeps the half of the list that must contain a peak, so the search runs
    in O(log(n)).
    """
    if not list_of_integers:
        return None
    low, high = 0, len(list_of_integers) - 1
    while low < high:
        mid = (low + high) // 2
        if list_of_integers[mid] < list_of_integers[mid + 1]:
            low = mid + 1
        else:
            high = mid
    return list_of_integers[low]
