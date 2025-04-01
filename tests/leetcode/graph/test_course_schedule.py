import pytest
from src.leetcode.graph.course_schedule import can_finish

def test_basic_case():
    """Test basic case with two courses."""
    num_courses = 2
    prerequisites = [[1, 0]]  # Course 1 depends on course 0
    assert can_finish(num_courses, prerequisites) is True
    
def test_cycle():
    """Test case with a cycle in prerequisites."""
    num_courses = 2
    prerequisites = [[1, 0], [0, 1]]  # Courses depend on each other
    assert can_finish(num_courses, prerequisites) is False
    
def test_no_prerequisites():
    """Test case with no prerequisites."""
    num_courses = 3
    prerequisites = []
    assert can_finish(num_courses, prerequisites) is True
    
def test_complex_dependencies():
    """Test case with more complex dependencies."""
    num_courses = 4
    prerequisites = [[1, 0], [2, 1], [3, 2]]  # Linear chain
    assert can_finish(num_courses, prerequisites) is True
    
def test_multiple_dependencies():
    """Test course with multiple prerequisites."""
    num_courses = 3
    prerequisites = [[2, 0], [2, 1]]  # Course 2 depends on 0 and 1
    assert can_finish(num_courses, prerequisites) is True
    
def test_complex_cycle():
    """Test case with a cycle in a larger graph."""
    num_courses = 4
    prerequisites = [[1, 0], [2, 1], [3, 2], [1, 3]]  # Cycle through multiple courses
    assert can_finish(num_courses, prerequisites) is False
    
def test_self_dependency():
    """Test course that depends on itself."""
    num_courses = 2
    prerequisites = [[1, 1]]  # Course depends on itself
    assert can_finish(num_courses, prerequisites) is False
    
def test_disconnected_components():
    """Test with multiple disconnected components."""
    num_courses = 4
    prerequisites = [[1, 0], [3, 2]]  # Two separate dependencies
    assert can_finish(num_courses, prerequisites) is True
    
def test_single_course():
    """Test with a single course."""
    num_courses = 1
    prerequisites = []
    assert can_finish(num_courses, prerequisites) is True
    
def test_all_courses_dependent():
    """Test where each course has a prerequisite."""
    num_courses = 3
    prerequisites = [[1, 0], [2, 1]]  # Each course depends on previous
    assert can_finish(num_courses, prerequisites) is True