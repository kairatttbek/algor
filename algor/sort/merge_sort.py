def merge_sort(arr):
    arr_len = len(arr)

    if arr_len <= 1:
        return arr

    mid = arr_len // 2

    left, right = arr[:mid], arr[mid:]

    merge_sort(left)
    merge_sort(right)

    i = j = 0
    for k in range(arr_len):
        if left[i] <= right[j]:
            arr[k] = left[i]
            i += 1
        else:
            arr[k] = right[j]
            j += 1

    # todo: copy left from left and right
