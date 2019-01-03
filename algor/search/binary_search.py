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
    return None
