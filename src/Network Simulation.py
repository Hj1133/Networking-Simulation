import networkx as nx
import matplotlib.pyplot as plt
from collections import deque

# Create a simple network topology
def create_network_topology():
    G = nx.Graph()

    # Add nodes (routers)
    G.add_node("Router1")
    G.add_node("Router2")
    G.add_node("Router3")
    G.add_node("Router4")
    
    # Add edges (links between routers with costs representing distances)
    G.add_edge("Router1", "Router2", weight=1)
    G.add_edge("Router1", "Router3", weight=4)
    G.add_edge("Router2", "Router3", weight=2)
    G.add_edge("Router3", "Router4", weight=3)
    G.add_edge("Router2", "Router4", weight=5)
    
    return G

# Function to visualize the network topology
def visualize_network(G):
    pos = nx.spring_layout(G)
    labels = nx.get_edge_attributes(G, 'weight')
    nx.draw(G, pos, with_labels=True, node_size=2000, node_color='lightblue')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)
    plt.show()

# Dijkstra's algorithm to find shortest path
def dijkstra_algorithm(G, start_node):
    # Dictionary to store the shortest path from start_node to all other nodes
    shortest_paths = {node: {"distance": float('inf'), "previous": None} for node in G.nodes()}
    shortest_paths[start_node]["distance"] = 0
    
    # List of all nodes to visit
    nodes_to_visit = deque([start_node])
    
    while nodes_to_visit:
        current_node = nodes_to_visit.popleft()
        
        for neighbor in G.neighbors(current_node):
            edge_weight = G[current_node][neighbor]["weight"]
            new_distance = shortest_paths[current_node]["distance"] + edge_weight
            
            if new_distance < shortest_paths[neighbor]["distance"]:
                shortest_paths[neighbor]["distance"] = new_distance
                shortest_paths[neighbor]["previous"] = current_node
                nodes_to_visit.append(neighbor)

    return shortest_paths

# Function to get the shortest path from start to end
def get_shortest_path(shortest_paths, start_node, end_node):
    path = []
    current_node = end_node
    while current_node is not None:
        path.append(current_node)
        current_node = shortest_paths[current_node]["previous"]
    return path[::-1]

# Main function to run the simulation
def run_network_simulation():
    # Step 1: Create network topology
    G = create_network_topology()
    
    # Step 2: Visualize network topology
    print("Network Topology:")
    visualize_network(G)
    
    # Step 3: Run Dijkstra's algorithm to find shortest paths from Router1
    start_node = "Router1"
    shortest_paths = dijkstra_algorithm(G, start_node)
    
    # Step 4: Print out the shortest paths from Router1 to all other routers
    print(f"\nShortest Paths from {start_node}:")
    for node in G.nodes():
        if node != start_node:
            path = get_shortest_path(shortest_paths, start_node, node)
            distance = shortest_paths[node]["distance"]
            print(f"To {node}: Path = {' -> '.join(path)}, Distance = {distance}")
    
    # Example of a specific route (Router1 to Router4)
    specific_path = get_shortest_path(shortest_paths, start_node, "Router4")
    specific_distance = shortest_paths["Router4"]["distance"]
    print(f"\nSpecific Path from Router1 to Router4: Path = {' -> '.join(specific_path)}, Distance = {specific_distance}")

if __name__ == "__main__":
    run_network_simulation()
