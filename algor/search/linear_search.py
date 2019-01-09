def linear_search(arr, target):
    """
    Liner search

    Complexity: O(n)
    """
    for i in range(len(arr)):
        if arr[i] == target:
            return i

    return -1
