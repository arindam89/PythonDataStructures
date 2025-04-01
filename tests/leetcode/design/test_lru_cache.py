import pytest
from src.leetcode.design.lru_cache import LRUCache

def test_basic_operations():
    """Test basic get/put operations."""
    cache = LRUCache(2)
    
    # Put some items
    cache.put(1, 1)
    cache.put(2, 2)
    assert cache.get(1) == 1
    
    # Evict least recently used item (key 2)
    cache.put(3, 3)
    assert cache.get(2) is None
    
    # Update existing key
    cache.put(1, 4)
    assert cache.get(1) == 4
    
def test_capacity_one():
    """Test with capacity of 1."""
    cache = LRUCache(1)
    cache.put(1, 1)
    cache.put(2, 2)
    assert cache.get(1) is None
    assert cache.get(2) == 2
    
def test_update_makes_recent():
    """Test that accessing an item makes it most recently used."""
    cache = LRUCache(2)
    cache.put(1, 1)
    cache.put(2, 2)
    
    # Access key 1, making it most recent
    assert cache.get(1) == 1
    
    # This should evict key 2 instead of key 1
    cache.put(3, 3)
    assert cache.get(1) == 1
    assert cache.get(2) is None
    assert cache.get(3) == 3
    
def test_update_existing():
    """Test updating existing keys."""
    cache = LRUCache(2)
    cache.put(1, 1)
    cache.put(2, 2)
    cache.put(1, 10)  # Update key 1
    assert cache.get(1) == 10
    assert cache.get(2) == 2
    
def test_eviction_order():
    """Test that items are evicted in LRU order."""
    cache = LRUCache(3)
    cache.put(1, 1)
    cache.put(2, 2)
    cache.put(3, 3)
    cache.get(1)  # Make 1 most recent
    cache.get(2)  # Make 2 most recent
    # 3 is now least recent
    
    cache.put(4, 4)  # Should evict 3
    assert cache.get(1) == 1
    assert cache.get(2) == 2
    assert cache.get(3) is None
    assert cache.get(4) == 4
    
def test_clear_cache():
    """Test clearing the cache."""
    cache = LRUCache(2)
    cache.put(1, 1)
    cache.put(2, 2)
    cache.clear()
    assert cache.get(1) is None
    assert cache.get(2) is None
    
def test_none_values():
    """Test storing None values."""
    cache = LRUCache(2)
    cache.put(1, None)
    assert cache.get(1) is None
    
    # Make sure we can distinguish between missing key and None value
    assert 1 in cache.cache
    assert 2 not in cache.cache
    
def test_type_flexibility():
    """Test that cache works with different value types."""
    cache = LRUCache[object](2)
    cache.put(1, "string")
    cache.put(2, 123)
    cache.put(3, [1, 2, 3])
    assert cache.get(1) is None  # Evicted
    assert cache.get(2) == 123
    assert cache.get(3) == [1, 2, 3]