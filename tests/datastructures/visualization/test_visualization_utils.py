import pytest
from src.datastructures.visualization.visualization_utils import VisualizationUtils
from src.datastructures.tree.tree_node import TreeNode
from src.datastructures.tree.binary_tree import BinaryTree
from src.datastructures.graph.graph import Graph
from src.datastructures.trie.trie import Trie
from src.datastructures.heap.min_heap import MinHeap
from src.datastructures.heap.max_heap import MaxHeap

class TestVisualizationUtils:
    """Test class for VisualizationUtils."""
    
    def test_visualize_binary_tree(self, tmp_path):
        """Test binary tree visualization."""
        # Create a simple binary tree
        root = TreeNode(1)
        root.left = TreeNode(2)
        root.right = TreeNode(3)
        root.left.left = TreeNode(4)
        root.left.right = TreeNode(5)
        
        # Visualize the tree
        filename = str(tmp_path / "test_tree")
        VisualizationUtils.visualize_binary_tree(root, filename)
        
        # Check if files were created
        assert (tmp_path / "test_tree").with_suffix(".gv").exists()
        assert (tmp_path / "test_tree").with_suffix(".gv.png").exists()
        
    def test_visualize_graph(self, tmp_path):
        """Test graph visualization."""
        # Create a simple graph
        graph = Graph(directed=True, weighted=True)
        vertices = ["A", "B", "C", "D"]
        edges = [("A", "B", 2), ("B", "C", 3), ("C", "D", 1), ("D", "A", 4)]
        
        for vertex in vertices:
            graph.add_vertex(vertex)
        for src, dst, weight in edges:
            graph.add_edge(src, dst, weight)
            
        # Visualize the graph
        filename = str(tmp_path / "test_graph")
        VisualizationUtils.visualize_graph(graph, filename)
        
        # Check if files were created
        assert (tmp_path / "test_graph").with_suffix(".gv").exists()
        assert (tmp_path / "test_graph").with_suffix(".gv.png").exists()
        
    def test_visualize_trie(self, tmp_path):
        """Test trie visualization."""
        # Create a simple trie
        trie = Trie()
        words = ["cat", "cats", "dog"]
        for word in words:
            trie.insert(word)
            
        # Visualize the trie
        filename = str(tmp_path / "test_trie")
        VisualizationUtils.visualize_trie(trie.root, filename)
        
        # Check if files were created
        assert (tmp_path / "test_trie").with_suffix(".gv").exists()
        assert (tmp_path / "test_trie").with_suffix(".gv.png").exists()
        
    def test_visualize_heap(self, tmp_path):
        """Test heap visualization."""
        # Create and populate a min heap
        min_heap = MinHeap()
        values = [4, 8, 2, 5, 1, 9, 3, 7, 6]
        for val in values:
            min_heap.insert(val)
            
        # Visualize the min heap
        filename = str(tmp_path / "test_min_heap")
        VisualizationUtils.visualize_heap(min_heap.heap, filename, is_min_heap=True)
        
        # Check if files were created
        assert (tmp_path / "test_min_heap").with_suffix(".gv").exists()
        assert (tmp_path / "test_min_heap").with_suffix(".gv.png").exists()
        
        # Create and populate a max heap
        max_heap = MaxHeap()
        values = [4, 8, 2, 5, 1, 9, 3, 7, 6]
        for val in values:
            max_heap.insert(val)
            
        # Visualize the max heap
        filename = str(tmp_path / "test_max_heap")
        VisualizationUtils.visualize_heap(max_heap.heap, filename, is_min_heap=False)
        
        # Check if files were created
        assert (tmp_path / "test_max_heap").with_suffix(".gv").exists()
        assert (tmp_path / "test_max_heap").with_suffix(".gv.png").exists()