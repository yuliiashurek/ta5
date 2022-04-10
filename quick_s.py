from collections import deque


def swap(arr, i, j):
    temp = arr[i]
    arr[i] = arr[j]
    arr[j] = temp


def partition(arr, start, end):
    # Pick the rightmost element as a pivot from the list
    pivot = arr[end]
    index = start

    for i in range(start, end):
        if arr[i] <= pivot:
            swap(arr, i, index)
            index = index + 1

    swap(arr, index, end)

    return index


# Iterative Quicksort

def iterative_quicksort(arr):
    # create a stack for storing sublist start and end index
    stack = deque()
    start = 0
    end = len(arr) - 1

    stack.append((start, end))

    # loop till stack is empty
    while stack:

        start, end = stack.pop()
        pivot = partition(arr, start, end)

        if pivot - 1 > start:
            stack.append((start, pivot - 1))

        if pivot + 1 < end:
            stack.append((pivot + 1, end))

    return stack
