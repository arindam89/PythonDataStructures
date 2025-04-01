from typing import TypeVar, Dict, Set, List, Optional, Generic
from collections import defaultdict, deque
from queue import PriorityQueue
from dataclasses import dataclass

T = TypeVar('T')

@dataclass
class VertexDistance(Generic[T]):
    """Helper class for Dijkstra's algorithm."""
    vertex: T
    distance: int

@dataclass
class Edge(Generic[T]):
    """Helper class for minimum spanning tree algorithm."""
    source: T
    destination: T
    weight: int

class Graph(Generic[T]):
    """
    Implementation of a graph data structure using an adjacency list.
    This implementation supports both directed and undirected graphs,
    as well as weighted edges.
    
    Time Complexity:
    - Add Vertex: O(1)
    - Add Edge: O(1)
    - Remove Vertex: O(V + E) where V is the number of vertices and E is the number of edges
    - Remove Edge: O(1)
    - BFS/DFS: O(V + E)
    
    Space Complexity: O(V + E) for the adjacency list
    """
    
    def __init__(self, directed: bool = False, weighted: bool = False):
        """
        Constructs a new graph.
        
        Args:
            directed: True if the graph is directed, False otherwise
            weighted: True if the graph is weighted, False otherwise
        """
        self.adjacency_list: Dict[T, Dict[T, int]] = {}
        self.directed = directed
        self.weighted = weighted
        
    def add_vertex(self, vertex: T) -> bool:
        """
        Adds a vertex to the graph.
        Time Complexity: O(1)
        
        Args:
            vertex: The vertex to add
            
        Returns:
            True if the vertex was added, False if it already exists
        """
        if vertex in self.adjacency_list:
            return False
            
        self.adjacency_list[vertex] = {}
        return True
        
    def add_edge(self, source: T, destination: T, weight: int = 1) -> bool:
        """
        Adds an edge between two vertices.
        Time Complexity: O(1)
        
        Args:
            source: The source vertex
            destination: The destination vertex
            weight: The weight of the edge (default is 1)
            
        Returns:
            True if the edge was added, False if either vertex doesn't exist
        """
        if source not in self.adjacency_list or destination not in self.adjacency_list:
            return False
            
        self.adjacency_list[source][destination] = weight
        if not self.directed:
            self.adjacency_list[destination][source] = weight
            
        return True
        
    def remove_vertex(self, vertex: T) -> bool:
        """
        Removes a vertex and all its edges from the graph.
        Time Complexity: O(V + E)
        
        Args:
            vertex: The vertex to remove
            
        Returns:
            True if the vertex was removed, False if it doesn't exist
        """
        if vertex not in self.adjacency_list:
            return False
            
        # Remove all edges pointing to this vertex
        for v in self.adjacency_list:
            self.adjacency_list[v].pop(vertex, None)
            
        # Remove the vertex and its edges
        del self.adjacency_list[vertex]
        return True
        
    def remove_edge(self, source: T, destination: T) -> bool:
        """
        Removes an edge between two vertices.
        Time Complexity: O(1)
        
        Args:
            source: The source vertex
            destination: The destination vertex
            
        Returns:
            True if the edge was removed, False if it doesn't exist
        """
        if source not in self.adjacency_list or destination not in self.adjacency_list:
            return False
            
        if destination not in self.adjacency_list[source]:
            return False
            
        del self.adjacency_list[source][destination]
        if not self.directed:
            del self.adjacency_list[destination][source]
            
        return True
        
    def get_vertices(self) -> Set[T]:
        """
        Gets all vertices in the graph.
        
        Returns:
            A set of all vertices
        """
        return set(self.adjacency_list.keys())
        
    def get_neighbors(self, vertex: T) -> Optional[Dict[T, int]]:
        """
        Gets all neighbors of a vertex.
        
        Args:
            vertex: The vertex to get neighbors for
            
        Returns:
            A dictionary mapping neighbors to edge weights, or None if vertex doesn't exist
        """
        if vertex not in self.adjacency_list:
            return None
        return dict(self.adjacency_list[vertex])
        
    def contains_vertex(self, vertex: T) -> bool:
        """
        Checks if the graph contains a vertex.
        
        Args:
            vertex: The vertex to check
            
        Returns:
            True if the vertex exists, False otherwise
        """
        return vertex in self.adjacency_list
        
    def contains_edge(self, source: T, destination: T) -> bool:
        """
        Checks if the graph contains an edge between two vertices.
        
        Args:
            source: The source vertex
            destination: The destination vertex
            
        Returns:
            True if the edge exists, False otherwise
        """
        if source not in self.adjacency_list or destination not in self.adjacency_list:
            return False
        return destination in self.adjacency_list[source]
        
    def bfs(self, start: T) -> List[T]:
        """
        Performs a breadth-first search starting from a given vertex.
        Time Complexity: O(V + E)
        
        Args:
            start: The vertex to start from
            
        Returns:
            A list of vertices in BFS order, or empty list if start vertex doesn't exist
        """
        if start not in self.adjacency_list:
            return []
            
        result = []
        visited = set()
        queue = deque([start])
        visited.add(start)
        
        while queue:
            vertex = queue.popleft()
            result.append(vertex)
            
            for neighbor in self.adjacency_list[vertex]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)
                    
        return result
        
    def dfs(self, start: T) -> List[T]:
        """
        Performs a depth-first search starting from a given vertex.
        Time Complexity: O(V + E)
        
        Args:
            start: The vertex to start from
            
        Returns:
            A list of vertices in DFS order, or empty list if start vertex doesn't exist
        """
        if start not in self.adjacency_list:
            return []
            
        result = []
        visited = set()
        
        def dfs_helper(vertex: T):
            visited.add(vertex)
            result.append(vertex)
            
            for neighbor in self.adjacency_list[vertex]:
                if neighbor not in visited:
                    dfs_helper(neighbor)
                    
        dfs_helper(start)
        return result
        
    def has_cycle(self) -> bool:
        """
        Checks if the graph has a cycle.
        The algorithm varies based on whether the graph is directed or undirected.
        
        Returns:
            True if the graph has a cycle, False otherwise
        """
        if self.directed:
            return self._has_directed_cycle()
        return self._has_undirected_cycle()
        
    def _has_undirected_cycle(self) -> bool:
        """Helper method to check for cycles in an undirected graph."""
        visited = set()
        
        def has_cycle_helper(vertex: T, parent: Optional[T]) -> bool:
            visited.add(vertex)
            
            for neighbor in self.adjacency_list[vertex]:
                if neighbor not in visited:
                    if has_cycle_helper(neighbor, vertex):
                        return True
                elif parent != neighbor:  # Found a back edge
                    return True
                    
            return False
            
        for vertex in self.adjacency_list:
            if vertex not in visited:
                if has_cycle_helper(vertex, None):
                    return True
                    
        return False
        
    def _has_directed_cycle(self) -> bool:
        """Helper method to check for cycles in a directed graph."""
        visited = set()
        rec_stack = set()
        
        def has_cycle_helper(vertex: T) -> bool:
            visited.add(vertex)
            rec_stack.add(vertex)
            
            for neighbor in self.adjacency_list[vertex]:
                if neighbor not in visited:
                    if has_cycle_helper(neighbor):
                        return True
                elif neighbor in rec_stack:  # Found a back edge
                    return True
                    
            rec_stack.remove(vertex)
            return False
            
        for vertex in self.adjacency_list:
            if vertex not in visited:
                if has_cycle_helper(vertex):
                    return True
                    
        return False
        
    def dijkstra(self, source: T) -> Optional[Dict[T, int]]:
        """
        Computes the shortest path from a source vertex to all other vertices.
        Time Complexity: O((V + E) log V)
        
        Args:
            source: The source vertex
            
        Returns:
            A dictionary mapping vertices to their shortest distance from source,
            or None if source vertex doesn't exist
        """
        if source not in self.adjacency_list:
            return None
            
        # Initialize distances
        distances = {vertex: float('inf') for vertex in self.adjacency_list}
        distances[source] = 0
        
        # Priority queue to store vertices and their distances
        pq = PriorityQueue()
        pq.put(VertexDistance(source, 0))
        processed = set()
        
        while not pq.empty():
            current = pq.get()
            vertex = current.vertex
            
            # Skip if we've processed this vertex
            if vertex in processed:
                continue
                
            processed.add(vertex)
            
            # Update distances to neighbors
            for neighbor, weight in self.adjacency_list[vertex].items():
                if neighbor in processed:
                    continue
                    
                new_distance = distances[vertex] + weight
                if new_distance < distances[neighbor]:
                    distances[neighbor] = new_distance
                    pq.put(VertexDistance(neighbor, new_distance))
                    
        return distances
        
    def minimum_spanning_tree(self) -> Optional['Graph[T]']:
        """
        Computes a minimum spanning tree using Prim's algorithm.
        Time Complexity: O((V + E) log V)
        
        Returns:
            A new graph representing the minimum spanning tree,
            or None if the graph is empty
        """
        if not self.adjacency_list:
            return None
            
        # Create a new graph for the MST
        mst = Graph[T](directed=False)
        
        # Add all vertices to the MST
        for vertex in self.adjacency_list:
            mst.add_vertex(vertex)
            
        # Set to keep track of vertices in MST
        in_mst = set()
        
        # Start with any vertex
        start = next(iter(self.adjacency_list))
        in_mst.add(start)
        
        # Priority queue to store edges
        pq = PriorityQueue()
        
        # Add edges from the start vertex
        for dest, weight in self.adjacency_list[start].items():
            pq.put(Edge(start, dest, weight))
            
        while not pq.empty() and len(in_mst) < len(self.adjacency_list):
            edge = pq.get()
            
            if edge.destination in in_mst:
                continue
                
            # Add the edge to MST
            mst.add_edge(edge.source, edge.destination, edge.weight)
            in_mst.add(edge.destination)
            
            # Add all edges from the new vertex
            for dest, weight in self.adjacency_list[edge.destination].items():
                if dest not in in_mst:
                    pq.put(Edge(edge.destination, dest, weight))
                    
        return mst
        
    def topological_sort(self) -> Optional[List[T]]:
        """
        Performs a topological sort of the graph.
        Only applicable to directed acyclic graphs (DAGs).
        Time Complexity: O(V + E)
        
        Returns:
            A list of vertices in topological order,
            or None if the graph has a cycle or is undirected
        """
        if not self.directed or self.has_cycle():
            return None
            
        result = []
        visited = set()
        
        def topo_sort_helper(vertex: T):
            visited.add(vertex)
            
            for neighbor in self.adjacency_list[vertex]:
                if neighbor not in visited:
                    topo_sort_helper(neighbor)
                    
            result.insert(0, vertex)
            
        for vertex in self.adjacency_list:
            if vertex not in visited:
                topo_sort_helper(vertex)
                
        return result
        
    def get_edge_weight(self, source: T, destination: T) -> int:
        """
        Gets the weight of an edge between two vertices.
        
        Args:
            source: The source vertex
            destination: The destination vertex
            
        Returns:
            The weight of the edge, or -1 if the edge doesn't exist
        """
        if not self.contains_edge(source, destination):
            return -1
        return self.adjacency_list[source][destination]
        
    def get_vertex_count(self) -> int:
        """Gets the number of vertices in the graph."""
        return len(self.adjacency_list)
        
    def get_edge_count(self) -> int:
        """Gets the number of edges in the graph."""
        count = sum(len(edges) for edges in self.adjacency_list.values())
        return count // 2 if not self.directed else count
        
    def is_directed(self) -> bool:
        """Returns whether the graph is directed."""
        return self.directed
        
    def is_weighted(self) -> bool:
        """Returns whether the graph is weighted."""
        return self.weighted