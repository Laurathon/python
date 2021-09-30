def list_check(lst):
    """Are all items in lst a list?

        >>> list_check([[1], [2, 3]])
        True

        >>> list_check([[1], "nope"])
        False
    """
    # return [True for items in lst if isinstance(items, list) else return False]
    for items in lst:
        if not isinstance(items, list):
            return False
    return True
