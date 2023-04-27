#!/usr/bin/env python3
"""Augment the following code with the correct duck-typed annotations:

# The types of the elements of the input are not know
def safe_first_element(lst):
    if lst:
        return lst[0]
    else:
        return None
    """


from typing import Any, List, Union


def safe_first_element(lst: List[Any]) -> Union[Any, None]:
    """
    Given a list `lst`, this function returns the first element of the list
    if it exists, and returns None if the list is empty.
    """
    if lst:
        return lst[0]
    else:
        return None
