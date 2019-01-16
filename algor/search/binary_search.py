def binary_search(array, target):
    """
    Iterative binary search
    Complexity: O(log n)
    """
    li, hi = 0, len(array) - 1
    while li <= hi:
        mi = (li + hi) // 2
        val = array[mi]
        if val == target:
            return mi
        elif val > target:
            hi = mi - 1
        else:
            li = mi + 1
    return -1


def recur_binary_search(array, target, li, hi):
    """
    Recursive binary search
    Complexity: O(log n)
    """
    if li > hi:
        return -1
    mi = (li + hi) // 2
    if array[mi] == target:
        return mi
    elif array[mi] > target:
        return recur_binary_search(array, target, li, mi - 1)
    else:
        return recur_binary_search(array, target, mi + 1, hi)
