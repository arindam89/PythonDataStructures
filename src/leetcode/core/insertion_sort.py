# Implementation of Insertion Sort in Python
# Problem: Implement the insertion sort algorithm.
# LeetCode Link: Not directly available, but this is a fundamental sorting algorithm.

def insertion_sort(arr):
    """Sort the array using insertion sort."""
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr