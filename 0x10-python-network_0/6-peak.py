#!/usr/bin/python3
"""find a peak in a list of unsorted integers"""


def find_peak(list_of_integers):
    """Finds a peak in list_of_integers"""

    if list_of_integers is None or list_of_integers == []:
        return None
    low = 0
    high = len(list_of_integers)
    meduim = ((high - low) // 2) + low
    meduim = int(meduim)
    if high == 1:
        return list_of_integers[0]
    if high == 2:
        return max(list_of_integers)
    if list_of_integers[meduim] >= list_of_integers[meduim - 1] and\
            list_of_integers[meduim] >= list_of_integers[meduim + 1]:
        return list_of_integers[meduim]
    if meduim > 0 and list_of_integers[meduim] < list_of_integers[meduim + 1]:
        return find_peak(list_of_integers[meduim:])
    if meduim > 0 and list_of_integers[meduim] < list_of_integers[meduim - 1]:
        return find_peak(list_of_integers[:meduim])
