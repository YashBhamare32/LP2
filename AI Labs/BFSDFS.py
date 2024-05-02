def bfs(graph, start, visited=None):
    """
    Breadth-First Search (BFS) traversal on a graph.
    """
    if visited is None:
        visited = set()
    queue = [start]
    visited.add(start)
    print("Node:", start, "Value:", graph[start]['value'])
    while queue:
        current = queue.pop(0)
        for neighbor in graph[current]['neighbors'] - visited:
            print("Node:", neighbor, "Value:", graph[neighbor]['value'])
            queue.append(neighbor)
            visited.add(neighbor)
    return visited

def dfs(graph, start, visited=None):
    """
    Depth-First Search (DFS) traversal on a graph.
    """
    if visited is None:
        visited = set()
    visited.add(start)
    print("Node:", start, "Value:", graph[start]['value'])
    for next_node in graph[start]['neighbors'] - visited:
        dfs(graph, next_node, visited)
    return visited

def create_graph():
    """
    Create a graph based on user input.
    """
    graph = {}
    num_nodes = int(input("Enter the number of nodes: "))
    for node_id in range(num_nodes):
        value = input(f"Enter value for node {node_id}: ")
        graph[str(node_id)] = {'value': value, 'neighbors': set()}
    num_edges = int(input("Enter the number of edges: "))
    for _ in range(num_edges):
        edge = input("Enter edge (format: from_node to_node): ").split()
        from_node, to_node = edge
        graph[from_node]['neighbors'].add(to_node)
    return graph

def main():
    """
    Main function to interact with the user and perform graph traversals.
    """
    graph = create_graph()
    while True:
        print("\nMenu:")
        print("1. Breadth-First Search (BFS)")
        print("2. Depth-First Search (DFS)")
        print("3. Reset Graph")
        print("4. Exit")
        choice = input("Enter your choice: ")
        if choice == '1':
            start_node = input("Enter the start node for BFS: ")
            print("BFS Traversal:")
            bfs(graph, start_node)
        elif choice == '2':
            start_node = input("Enter the start node for DFS: ")
            print("DFS Traversal:")
            dfs(graph, start_node)
        elif choice == '3':
            print("Resetting graph.")
            graph = create_graph()
        elif choice == '4':
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Please enter a valid option.")

if __name__ == "__main__":
    main()
