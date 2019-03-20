def merge_sort(arr):
    if len(arr) <= 1:
        return

    mid = len(arr) // 2

    left, right = arr[:mid], arr[mid:]

    merge_sort(left)
    merge_sort(right)

    k = i = j = 0
    for k in range(len(arr)):
        if left[i] <= right[j]:
            arr[k] = left[i]
            i += 1
        else:
            arr[k] = right[j]
            j += 1
        k += 1

    while i < len(left):
        arr[k] = left[i]
        i += 1
        k += 1

    while j < len(right):
        arr[k] = right[j]
        j += 1
        k += 1
