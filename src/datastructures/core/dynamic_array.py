# Implementation of a Dynamic Array (Resizable Array) in Python
# Problem: Design a dynamic array that supports operations like append, insert, delete, and resizing.
# LeetCode Link: Not directly available, but this is a fundamental data structure.

class DynamicArray:
    def __init__(self):
        """Initialize the dynamic array with an initial capacity of 1."""
        self.capacity = 1
        self.size = 0
        self.array = [None] * self.capacity

    def append(self, value):
        """Add an element to the end of the array."""
        if self.size == self.capacity:
            self._resize(2 * self.capacity)
        self.array[self.size] = value
        self.size += 1

    def insert(self, index, value):
        """Insert an element at a specific index."""
        if index < 0 or index > self.size:
            raise IndexError("Index out of bounds")
        if self.size == self.capacity:
            self._resize(2 * self.capacity)
        for i in range(self.size, index, -1):
            self.array[i] = self.array[i - 1]
        self.array[index] = value
        self.size += 1

    def delete(self, index):
        """Delete an element at a specific index."""
        if index < 0 or index >= self.size:
            raise IndexError("Index out of bounds")
        for i in range(index, self.size - 1):
            self.array[i] = self.array[i + 1]
        self.array[self.size - 1] = None
        self.size -= 1
        if self.size > 0 and self.size == self.capacity // 4:
            self._resize(self.capacity // 2)

    def _resize(self, new_capacity):
        """Resize the array to a new capacity."""
        new_array = [None] * new_capacity
        for i in range(self.size):
            new_array[i] = self.array[i]
        self.array = new_array
        self.capacity = new_capacity

    def __getitem__(self, index):
        """Get an element at a specific index."""
        if index < 0 or index >= self.size:
            raise IndexError("Index out of bounds")
        return self.array[index]

    def __len__(self):
        """Return the number of elements in the array."""
        return self.size

    def __str__(self):
        """Return a string representation of the array."""
        return str([self.array[i] for i in range(self.size)])