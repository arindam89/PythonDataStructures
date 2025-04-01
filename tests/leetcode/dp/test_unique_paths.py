import pytest
from PythonDataStructures.src.leetcode.dynamic_programming_2d.unique_paths import unique_paths

def test_unique_paths():
    # Test case 1: 3x7 grid
    assert unique_paths(3, 7) == 28

    # Test case 2: 3x2 grid
    assert unique_paths(3, 2) == 3

    # Test case 3: 7x3 grid
    assert unique_paths(7, 3) == 28

    # Test case 4: 3x3 grid
    assert unique_paths(3, 3) == 6

    # Test case 5: 1x1 grid
    assert unique_paths(1, 1) == 1
```
# Move this file to the dynamic_programming_2d folder.