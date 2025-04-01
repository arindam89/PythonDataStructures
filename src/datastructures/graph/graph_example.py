"""Example module to demonstrate the usage of Graph implementation."""

from .graph import Graph
from typing import Dict, List

def run_example() -> None:
    """
    Runs examples demonstrating graph operations.
    Shows various graph operations including traversal, cycle detection,
    shortest paths, and minimum spanning tree computation.
    """
    # Example 1: Undirected Graph
    print("Undirected Graph Example:")
    
    # Create an undirected graph
    undirected_graph = Graph()
    
    # Add vertices
    print("Adding vertices: A, B, C, D, E")
    vertices = ["A", "B", "C", "D", "E"]
    for vertex in vertices:
        undirected_graph.add_vertex(vertex)
    
    # Add edges
    print("Adding edges: A-B(2), A-C(3), B-D(1), C-D(5), D-E(4)")
    edges = [("A", "B", 2), ("A", "C", 3), ("B", "D", 1), 
            ("C", "D", 5), ("D", "E", 4)]
    for source, dest, weight in edges:
        undirected_graph.add_edge(source, dest, weight)
    
    # Example 2: Graph Traversals
    print("\nGraph Traversals:")
    
    # BFS traversal
    bfs_result = undirected_graph.bfs("A")
    print(f"BFS starting from A: {bfs_result}")
    
    # DFS traversal
    dfs_result = undirected_graph.dfs("A")
    print(f"DFS starting from A: {dfs_result}")
    
    # Example 3: Graph Operations
    print("\nGraph Operations:")
    
    # Check vertices and edges
    print(f"Contains vertex A? {undirected_graph.contains_vertex('A')}")
    print(f"Contains vertex F? {undirected_graph.contains_vertex('F')}")
    print(f"Contains edge A-B? {undirected_graph.contains_edge('A', 'B')}")
    print(f"Contains edge A-D? {undirected_graph.contains_edge('A', 'D')}")
    
    # Get neighbors
    neighbors = undirected_graph.get_neighbors("A")
    print(f"Neighbors of A: {neighbors}")
    
    # Get edge weight
    weight = undirected_graph.get_edge_weight("A", "B")
    print(f"Weight of edge A-B: {weight}")
    
    # Check if the undirected graph has a cycle
    has_cycle = undirected_graph.has_cycle()
    print(f"Undirected graph has cycle? {has_cycle}")
    
    # Create a tree-like undirected graph (no cycles)
    print("\nCreating a tree-like undirected graph (no cycles):")
    tree = Graph()
    tree.add_vertex("A")
    tree.add_vertex("B")
    tree.add_vertex("C")
    tree.add_vertex("D")
    tree.add_edge("A", "B", 1)
    tree.add_edge("B", "C", 1)
    tree.add_edge("C", "D", 1)
    print(f"Tree-like undirected graph has cycle? {tree.has_cycle()}")
    
    # Example 4: Directed Graph
    print("\nDirected Graph Example:")
    
    # Create a directed graph
    directed_graph = Graph(directed=True)
    
    # Add vertices and edges
    print("Adding vertices: A, B, C, D")
    for vertex in ["A", "B", "C", "D"]:
        directed_graph.add_vertex(vertex)
    
    print("Adding edges: A->B, A->C, B->C, C->D, D->A")
    directed_edges = [("A", "B"), ("A", "C"), ("B", "C"), 
                     ("C", "D"), ("D", "A")]
    for source, dest in directed_edges:
        directed_graph.add_edge(source, dest)
    
    # Check if the directed graph has a cycle
    has_cycle = directed_graph.has_cycle()
    print(f"Directed graph has cycle? {has_cycle}")
    
    # Example 5: Directed Acyclic Graph (DAG)
    print("\nDirected Acyclic Graph (DAG) Example:")
    dag = Graph(directed=True)
    
    # Add vertices and edges to form a DAG
    for vertex in ["A", "B", "C", "D", "E"]:
        dag.add_vertex(vertex)
    
    dag_edges = [("A", "B"), ("A", "C"), ("B", "D"), ("C", "D"), ("D", "E")]
    for source, dest in dag_edges:
        dag.add_edge(source, dest)
    
    # Perform topological sort
    topo_order = dag.topological_sort()
    print(f"Topological sort order: {topo_order}")
    
    # Example 6: Shortest Paths (Dijkstra's Algorithm)
    print("\nShortest Paths Example:")
    distances = undirected_graph.dijkstra("A")
    print("Shortest paths from A:")
    for vertex, distance in distances.items():
        print(f"  To {vertex}: {distance}")
    
    # Example 7: Minimum Spanning Tree
    print("\nMinimum Spanning Tree Example:")
    mst = undirected_graph.minimum_spanning_tree()
    print(f"MST edge count: {mst.get_edge_count()}")
    print(f"MST has cycle? {mst.has_cycle()}")
    
    # Example 8: Graph Modifications
    print("\nGraph Modification Example:")
    print("Removing edge B-D...")
    undirected_graph.remove_edge("B", "D")
    print(f"Edge B-D exists? {undirected_graph.contains_edge('B', 'D')}")
    
    print("\nRemoving vertex C...")
    undirected_graph.remove_vertex("C")
    print(f"Vertex C exists? {undirected_graph.contains_vertex('C')}")
    print(f"Edge A-C exists? {undirected_graph.contains_edge('A', 'C')}")

if __name__ == "__main__":
    run_example()