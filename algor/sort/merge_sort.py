def merge_sort(arr):
    """
    Merge sort
    Complexity: O(n log(n))
    """

    if len(arr) <= 1:
        return

    mid = len(arr) // 2

    L, R = arr[:mid], arr[mid:]

    merge_sort(L)
    merge_sort(R)

    k = i = j = 0

    while i < len(L) and j < len(R):
        if L[i] <= R[j]:
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = R[j]
            j += 1
        k += 1

    while i < len(L):
        arr[k] = L[i]
        i += 1
        k += 1

    while j < len(R):
        arr[k] = R[j]
        j += 1
        k += 1
