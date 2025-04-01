import pytest
from src.datastructures.trie.trie import Trie

class TestTrie:
    """Test class for Trie implementation."""
    
    @pytest.fixture
    def empty_trie(self):
        """Fixture that provides an empty trie."""
        return Trie()
        
    @pytest.fixture
    def populated_trie(self):
        """Fixture that provides a populated trie."""
        trie = Trie()
        words = ["cat", "cats", "cattle", "dog", "dogs", "dove"]
        for word in words:
            trie.insert(word)
        return trie, words
        
    def test_empty_trie(self, empty_trie):
        """Test operations on an empty trie."""
        assert empty_trie.is_empty()
        assert empty_trie.size() == 0
        assert not empty_trie.search("word")
        assert not empty_trie.starts_with("wo")
        assert empty_trie.get_all_words() == []
        
    def test_insert_and_search(self, empty_trie):
        """Test insert and search operations."""
        assert not empty_trie.search("cat")
        
        empty_trie.insert("cat")
        assert empty_trie.search("cat")
        assert not empty_trie.search("cats")
        assert empty_trie.size() == 1
        
        # Insert same word again should not increase size
        empty_trie.insert("cat")
        assert empty_trie.size() == 1
        
    def test_starts_with(self, populated_trie):
        """Test prefix searching."""
        trie, _ = populated_trie
        
        # Test existing prefixes
        assert trie.starts_with("cat")
        assert trie.starts_with("do")
        assert trie.starts_with("")  # Empty prefix
        
        # Test non-existing prefixes
        assert not trie.starts_with("bir")
        assert not trie.starts_with("e")
        
    def test_remove(self, populated_trie):
        """Test remove operation."""
        trie, words = populated_trie
        initial_size = trie.size()
        
        # Remove existing word
        assert trie.remove("cat")
        assert not trie.search("cat")
        assert trie.search("cats")  # Other words with same prefix should remain
        assert trie.size() == initial_size - 1
        
        # Remove non-existing word
        assert not trie.remove("car")
        assert trie.size() == initial_size - 1
        
        # Remove all words
        for word in words:
            trie.remove(word)
        assert trie.is_empty()
        
    def test_get_words_with_prefix(self, populated_trie):
        """Test retrieving words with a given prefix."""
        trie, _ = populated_trie
        
        # Test with existing prefixes
        assert set(trie.get_words_with_prefix("cat")) == {"cat", "cats", "cattle"}
        assert set(trie.get_words_with_prefix("do")) == {"dog", "dogs", "dove"}
        
        # Test with complete words as prefix
        assert set(trie.get_words_with_prefix("dog")) == {"dog", "dogs"}
        
        # Test with non-existing prefix
        assert trie.get_words_with_prefix("x") == []
        
        # Test with empty prefix (should return all words)
        assert set(trie.get_words_with_prefix("")) == {"cat", "cats", "cattle", 
                                                      "dog", "dogs", "dove"}
        
    def test_get_all_words(self, populated_trie):
        """Test retrieving all words."""
        trie, words = populated_trie
        assert set(trie.get_all_words()) == set(words)
        
    def test_clear(self, populated_trie):
        """Test clear operation."""
        trie, _ = populated_trie
        assert not trie.is_empty()
        
        trie.clear()
        assert trie.is_empty()
        assert trie.size() == 0
        assert trie.get_all_words() == []
        
    def test_size_and_empty(self, empty_trie):
        """Test size and empty status."""
        assert empty_trie.is_empty()
        assert empty_trie.size() == 0
        
        empty_trie.insert("word")
        assert not empty_trie.is_empty()
        assert empty_trie.size() == 1
        
        empty_trie.remove("word")
        assert empty_trie.is_empty()
        assert empty_trie.size() == 0