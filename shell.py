def shellsort(arr, n):
    step = n // 2
    while step > 0:
        for i in range(step, n):
            temp = arr[i]
            j = i
            while j >= step and arr[j - step] > temp:
                arr[j] = arr[j - step]
                j -= step

            arr[j] = temp
        step //= 2
    return arr
