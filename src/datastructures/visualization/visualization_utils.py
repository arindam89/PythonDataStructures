"""Utilities for visualizing data structures."""

import graphviz
from typing import Optional, Any, Dict
from ..tree.tree_node import TreeNode
from ..graph.graph import Graph

class VisualizationUtils:
    """Utility class for visualizing various data structures."""
    
    @staticmethod
    def visualize_binary_tree(root: Optional[TreeNode], filename: str = "tree") -> None:
        """
        Create a visualization of a binary tree using graphviz.
        
        Args:
            root: The root node of the tree
            filename: The name of the output file (without extension)
        """
        dot = graphviz.Digraph()
        dot.attr(rankdir='TB')
        
        def add_nodes(node: TreeNode, node_id: str = "0") -> None:
            if not node:
                return
                
            # Add current node
            dot.node(node_id, str(node.val))
            
            # Add left child
            if node.left:
                left_id = f"{node_id}L"
                dot.node(left_id, str(node.left.val))
                dot.edge(node_id, left_id)
                add_nodes(node.left, left_id)
                
            # Add right child
            if node.right:
                right_id = f"{node_id}R"
                dot.node(right_id, str(node.right.val))
                dot.edge(node_id, right_id)
                add_nodes(node.right, right_id)
                
        if root:
            add_nodes(root)
            dot.render(filename, view=True, format='png')
            
    @staticmethod
    def visualize_graph(graph: Graph, filename: str = "graph") -> None:
        """
        Create a visualization of a graph using graphviz.
        
        Args:
            graph: The graph to visualize
            filename: The name of the output file (without extension)
        """
        dot = graphviz.Digraph() if graph.is_directed() else graphviz.Graph()
        dot.attr(rankdir='LR')
        
        # Add all vertices
        for vertex in graph.get_vertices():
            dot.node(str(vertex), str(vertex))
            
        # Add all edges
        added_edges = set()  # For undirected graphs to avoid duplicate edges
        for vertex in graph.get_vertices():
            neighbors = graph.get_neighbors(vertex)
            if neighbors:
                for neighbor, weight in neighbors.items():
                    if not graph.is_directed():
                        edge = tuple(sorted([str(vertex), str(neighbor)]))
                        if edge in added_edges:
                            continue
                        added_edges.add(edge)
                        
                    dot.edge(str(vertex), str(neighbor), 
                            label=str(weight) if graph.is_weighted() else "")
                            
        dot.render(filename, view=True, format='png')
        
    @staticmethod
    def visualize_trie(root: Any, filename: str = "trie") -> None:
        """
        Create a visualization of a trie using graphviz.
        
        Args:
            root: The root node of the trie
            filename: The name of the output file (without extension)
        """
        dot = graphviz.Digraph()
        dot.attr(rankdir='TB')
        
        def add_nodes(node: Any, node_id: str = "0", 
                     path_from_root: str = "") -> None:
            # Add current node
            label = "ROOT" if node_id == "0" else path_from_root[-1]
            if hasattr(node, 'is_end_of_word') and node.is_end_of_word:
                label += "*"
            dot.node(node_id, label)
            
            # Add children
            if hasattr(node, 'children'):
                for char, child in node.children.items():
                    child_id = f"{node_id}_{char}"
                    add_nodes(child, child_id, path_from_root + char)
                    dot.edge(node_id, child_id)
                    
        add_nodes(root)
        dot.render(filename, view=True, format='png')
        
    @staticmethod
    def visualize_heap(heap: List[int], filename: str = "heap", is_min_heap: bool = True) -> None:
        """
        Create a visualization of a heap using graphviz.
        
        Args:
            heap: The heap array to visualize
            filename: The name of the output file (without extension)
            is_min_heap: True if this is a min heap, False for max heap
        """
        if not heap:
            return
            
        dot = graphviz.Digraph()
        dot.attr(rankdir='TB')
        
        def add_nodes(index: int = 0) -> None:
            if index >= len(heap):
                return
                
            # Add current node
            dot.node(str(index), str(heap[index]))
            
            # Add left child
            left = 2 * index + 1
            if left < len(heap):
                dot.edge(str(index), str(left))
                add_nodes(left)
                
            # Add right child
            right = 2 * index + 2
            if right < len(heap):
                dot.edge(str(index), str(right))
                add_nodes(right)
                
        add_nodes()
        dot.render(filename, view=True, format='png')