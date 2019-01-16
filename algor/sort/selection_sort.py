def selection_sort(arr):
    """
    Selection sort
    Complexity: O(n^2)
    """
    arr_len = len(arr)
    for i in range(arr_len):
        min_idx = i
        for j in range(i + 1, arr_len):
            if arr[min_idx] > arr[j]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]

    return arr
