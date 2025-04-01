import pytest
from src.datastructures.graph.graph import Graph

class TestGraph:
    """Test class for Graph implementation."""
    
    @pytest.fixture
    def undirected_graph(self):
        """Fixture for an undirected graph."""
        graph = Graph()
        
        # Add vertices
        graph.add_vertex("A")
        graph.add_vertex("B")
        graph.add_vertex("C")
        graph.add_vertex("D")
        graph.add_vertex("E")
        
        # Add edges
        graph.add_edge("A", "B", 2)
        graph.add_edge("A", "C", 3)
        graph.add_edge("B", "D", 1)
        graph.add_edge("C", "D", 5)
        graph.add_edge("D", "E", 4)
        
        return graph
        
    @pytest.fixture
    def directed_graph(self):
        """Fixture for a directed graph."""
        graph = Graph(directed=True)
        
        # Add vertices
        graph.add_vertex("A")
        graph.add_vertex("B")
        graph.add_vertex("C")
        graph.add_vertex("D")
        graph.add_vertex("E")
        
        # Add edges
        graph.add_edge("A", "B", 2)
        graph.add_edge("A", "C", 3)
        graph.add_edge("B", "D", 1)
        graph.add_edge("C", "D", 5)
        graph.add_edge("D", "E", 4)
        
        return graph
        
    def test_add_vertex(self, undirected_graph):
        """Test adding vertices."""
        # Test adding a new vertex
        assert undirected_graph.add_vertex("F")
        assert undirected_graph.contains_vertex("F")
        
        # Test adding an existing vertex
        assert not undirected_graph.add_vertex("A")
        
    def test_add_edge(self, undirected_graph):
        """Test adding edges."""
        # Test adding a new edge
        assert undirected_graph.add_edge("A", "E", 6)
        assert undirected_graph.contains_edge("A", "E")
        assert undirected_graph.contains_edge("E", "A")
        assert undirected_graph.get_edge_weight("A", "E") == 6
        
        # Test adding edge with default weight
        assert undirected_graph.add_edge("B", "C")
        assert undirected_graph.contains_edge("B", "C")
        assert undirected_graph.get_edge_weight("B", "C") == 1
        
        # Test adding edge with non-existent vertices
        assert not undirected_graph.add_edge("A", "F")
        assert not undirected_graph.add_edge("F", "A")
        assert not undirected_graph.add_edge("F", "G")
        
    def test_remove_vertex(self, undirected_graph):
        """Test removing vertices."""
        # Test removing an existing vertex
        assert undirected_graph.remove_vertex("C")
        assert not undirected_graph.contains_vertex("C")
        assert not undirected_graph.contains_edge("A", "C")
        assert not undirected_graph.contains_edge("C", "D")
        
        # Test removing a non-existent vertex
        assert not undirected_graph.remove_vertex("F")
        
    def test_remove_edge(self, undirected_graph):
        """Test removing edges."""
        # Test removing an existing edge
        assert undirected_graph.remove_edge("A", "B")
        assert not undirected_graph.contains_edge("A", "B")
        assert not undirected_graph.contains_edge("B", "A")
        
        # Test removing a non-existent edge
        assert not undirected_graph.remove_edge("A", "E")
        assert not undirected_graph.remove_edge("A", "F")
        assert not undirected_graph.remove_edge("F", "A")
        
    def test_get_neighbors(self, undirected_graph):
        """Test getting neighbors of vertices."""
        # Test getting neighbors of an existing vertex
        neighbors = undirected_graph.get_neighbors("A")
        assert neighbors is not None
        assert len(neighbors) == 2
        assert "B" in neighbors
        assert "C" in neighbors
        assert neighbors["B"] == 2
        assert neighbors["C"] == 3
        
        # Test getting neighbors of a vertex with no neighbors
        undirected_graph.add_vertex("F")
        neighbors = undirected_graph.get_neighbors("F")
        assert neighbors is not None
        assert len(neighbors) == 0
        
        # Test getting neighbors of a non-existent vertex
        assert undirected_graph.get_neighbors("G") is None
        
    def test_traversals(self, undirected_graph):
        """Test graph traversal algorithms."""
        # Test BFS
        bfs_result = undirected_graph.bfs("A")
        assert len(bfs_result) == 5
        assert bfs_result[0] == "A"
        
        # Test BFS from non-existent vertex
        assert undirected_graph.bfs("F") == []
        
        # Test DFS
        dfs_result = undirected_graph.dfs("A")
        assert len(dfs_result) == 5
        assert dfs_result[0] == "A"
        
        # Test DFS from non-existent vertex
        assert undirected_graph.dfs("F") == []
        
    def test_has_cycle(self, undirected_graph, directed_graph):
        """Test cycle detection."""
        # Test cycle in undirected graph
        assert undirected_graph.has_cycle()
        
        # Create an acyclic undirected graph (tree)
        tree = Graph()
        tree.add_vertex("A")
        tree.add_vertex("B")
        tree.add_vertex("C")
        tree.add_vertex("D")
        tree.add_edge("A", "B")
        tree.add_edge("B", "C")
        tree.add_edge("C", "D")
        assert not tree.has_cycle()
        
        # Test cycle in directed graph
        assert not directed_graph.has_cycle()
        
        # Create a cyclic directed graph
        directed_graph.add_edge("E", "A")
        assert directed_graph.has_cycle()
        
    def test_dijkstra(self, undirected_graph):
        """Test Dijkstra's shortest path algorithm."""
        distances = undirected_graph.dijkstra("A")
        assert distances is not None
        assert len(distances) == 5
        assert distances["A"] == 0
        assert distances["B"] == 2
        assert distances["C"] == 3
        assert distances["D"] == 3  # A->B->D is shorter than A->C->D
        assert distances["E"] == 7  # A->B->D->E
        
        # Test Dijkstra from non-existent vertex
        assert undirected_graph.dijkstra("F") is None
        
    def test_minimum_spanning_tree(self, undirected_graph):
        """Test minimum spanning tree computation."""
        mst = undirected_graph.minimum_spanning_tree()
        assert mst is not None
        assert mst.get_vertex_count() == 5
        assert mst.get_edge_count() == 4  # MST has V-1 edges
        assert not mst.has_cycle()
        
        # Test MST of empty graph
        empty_graph = Graph()
        assert empty_graph.minimum_spanning_tree() is None
        
    def test_topological_sort(self, directed_graph):
        """Test topological sort."""
        # Test on acyclic directed graph
        topo_sort = directed_graph.topological_sort()
        assert topo_sort is not None
        assert len(topo_sort) == 5
        assert topo_sort[0] == "A"  # A should be first as it has no incoming edges
        assert topo_sort[-1] == "E"  # E should be last as it has no outgoing edges
        
        # Test on cyclic directed graph
        directed_graph.add_edge("E", "A")
        assert directed_graph.topological_sort() is None
        
        # Test on undirected graph
        assert undirected_graph.topological_sort() is None
        
    def test_get_edge_weight(self, undirected_graph):
        """Test getting edge weights."""
        assert undirected_graph.get_edge_weight("A", "B") == 2
        assert undirected_graph.get_edge_weight("B", "A") == 2  # Undirected
        assert undirected_graph.get_edge_weight("A", "E") == -1  # Non-existent edge
        assert undirected_graph.get_edge_weight("A", "F") == -1  # Non-existent vertex
        
    def test_counts(self, undirected_graph, directed_graph):
        """Test vertex and edge counting."""
        # Test vertex count
        assert undirected_graph.get_vertex_count() == 5
        undirected_graph.add_vertex("F")
        assert undirected_graph.get_vertex_count() == 6
        undirected_graph.remove_vertex("F")
        assert undirected_graph.get_vertex_count() == 5
        
        # Test edge count
        assert undirected_graph.get_edge_count() == 5  # Each edge counted once
        assert directed_graph.get_edge_count() == 5  # Direction matters