# Python Data Structures and Algorithms

This is a Python port of the Java Data Structures implementation. It contains:
- Common data structures implementations
- LeetCode problem solutions
- Test cases using pytest
- Visualization utilities for data structures

## Project Structure
```
PythonDataStructures/
├── src/
│   ├── datastructures/          # Core data structure implementations
│   │   ├── bst/                 # Binary Search Tree
│   │   ├── graph/               # Graph algorithms
│   │   ├── heap/               # Min and Max Heap
│   │   ├── linkedlist/         # Linked List
│   │   ├── tree/              # Binary Tree
│   │   ├── trie/              # Trie data structure
│   │   └── visualization/     # Visualization utilities
│   └── leetcode/               # LeetCode solutions by category
│       ├── arrays/
│       ├── backtracking/
│       ├── bit/
│       ├── design/
│       ├── dp/                # Dynamic Programming
│       ├── graph/
│       ├── string/
│       └── tree/
├── tests/                      # Corresponding test files
│   ├── datastructures/
│   └── leetcode/
├── requirements.txt
└── README.md
```

## Features
- **Data Structures**: Comprehensive implementation of fundamental data structures
  - Binary Search Tree (BST)
  - Graph with common algorithms
  - Min/Max Heaps
  - Linked List
  - Binary Tree
  - Trie
  - Visualization utilities for data structures
- **LeetCode Solutions**: Organized by categories
  - Array manipulation
  - Backtracking algorithms
  - Bit manipulation
  - System design problems
  - Dynamic programming
  - Graph algorithms
  - String manipulation
  - Tree-based problems

## Dependencies
- pytest & pytest-cov - For testing and code coverage
- graphviz - For generating visual representations of data structures
- matplotlib - For plotting and visualization
- networkx - For advanced graph operations and visualization

## Setup
1. Create a virtual environment: `python -m venv venv`
2. Activate it: 
   - Windows: `venv\Scripts\activate`
   - Unix/MacOS: `source venv/bin/activate`
3. Install dependencies: `pip install -r requirements.txt`

## Running Tests
- Run all tests: `pytest`
- Run specific test file: `pytest tests/path/to/test_file.py`
- Run tests with coverage: `pytest --cov=src tests/`
- Run tests for specific module: `pytest tests/datastructures/bst/` or `pytest tests/leetcode/arrays/`
