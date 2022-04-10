# partitioning elements into two sub-arrays

def partition(array, low, high):
    pivot = array[high]
    i = low - 1

    for j in range(low, high):
        if array[j] <= pivot:
            i = i + 1
            (array[i], array[j]) = (array[j], array[i])

    (array[i + 1], array[high]) = (array[high], array[i + 1])

    return i + 1


def quick_sort(array, low, high):
    if low < high:
        pi = partition(array, low, high)

        # recursive call on the left of pivot
        quick_sort(array, low, pi - 1)

        # recursive call on the right of pivot
        quick_sort(array, pi + 1, high)
    return array


