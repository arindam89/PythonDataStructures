# Implementation of a Dynamic Array (Resizable Array) in Python
# Problem Description:
# A dynamic array is an array that resizes itself as elements are added or removed.
# It provides random access to elements and supports operations like append, insert, delete, etc.

class DynamicArray:
    def __init__(self):
        """Initialize the dynamic array with an initial capacity of 1."""
        self.capacity = 1  # Initial capacity of the array
        self.size = 0      # Number of elements in the array
        self.array = [None] * self.capacity

    def append(self, value):
        """Add an element to the end of the array."""
        if self.size == self.capacity:
            self._resize(2 * self.capacity)  # Double the capacity if the array is full
        self.array[self.size] = value
        self.size += 1

    def _resize(self, new_capacity):
        """Resize the array to a new capacity."""
        new_array = [None] * new_capacity
        for i in range(self.size):
            new_array[i] = self.array[i]
        self.array = new_array
        self.capacity = new_capacity

    def get(self, index):
        """Get the element at a specific index."""
        if index < 0 or index >= self.size:
            raise IndexError("Index out of bounds")
        return self.array[index]

    def remove(self, index):
        """Remove the element at a specific index."""
        if index < 0 or index >= self.size:
            raise IndexError("Index out of bounds")
        for i in range(index, self.size - 1):
            self.array[i] = self.array[i + 1]
        self.array[self.size - 1] = None
        self.size -= 1
        if self.size > 0 and self.size == self.capacity // 4:
            self._resize(self.capacity // 2)  # Shrink the capacity if necessary

    def __len__(self):
        """Return the number of elements in the array."""
        return self.size

    def __str__(self):
        """Return a string representation of the array."""
        return str([self.array[i] for i in range(self.size)])

# Example Usage:
# dynamic_array = DynamicArray()
# dynamic_array.append(1)
# dynamic_array.append(2)
# dynamic_array.append(3)
# print(dynamic_array)  # Output: [1, 2, 3]
# dynamic_array.remove(1)
# print(dynamic_array)  # Output: [1, 3]
# print(dynamic_array.get(0))  # Output: 1