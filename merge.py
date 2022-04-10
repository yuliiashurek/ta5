def merge_sort(arr):
    if len(arr) > 1:
        middle = len(arr) // 2

        left = arr[:middle]
        right = arr[middle:]

        merge_sort(left)
        merge_sort(right)

        i = j = k = 0

        # Copy data to temp arrays L[] and R[]
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
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

    return arr
