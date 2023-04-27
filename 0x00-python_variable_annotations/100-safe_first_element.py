from typing import Sequence, Optional


def safe_first_element(lst: Sequence[Any]) -> Optional[Any]:
    """
    Returns the first element of a sequence or None if the sequence is empty.

    Args:
        lst (Sequence): The sequence to extract the first element from.

    Returns:
        Any: The first element of the sequence, or None if the
        sequence is empty.
    """
    if lst:
        return lst[0]
    else:
        return None
