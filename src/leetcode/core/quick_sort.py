# Implementation of Quick Sort in Python
# Problem: Implement the quick sort algorithm.
# LeetCode Link: Not directly available, but this is a fundamental sorting algorithm.

def quick_sort(arr):
    """Sort the array using quick sort."""
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)