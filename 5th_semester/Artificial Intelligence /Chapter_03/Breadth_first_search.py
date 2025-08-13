from collections import deque

# Define the graph as an adjacency list (dictionary)
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['G'],
    'F': [],
    'G': []
}

# Function to perform BFS
def bfs(graph, start, goal):
    # Create a queue to store nodes to visit
    queue = deque([start])
    # Set to keep track of visited nodes
    visited = set()

    # While there are nodes to visit
    while queue:
        node = queue.popleft()  # Pop the leftmost element
        print(f"Visiting: {node}")

        # If the node is the goal, return it
        if node == goal:
            print(f"Goal '{goal}' found!")
            return node

        # If the node has not been visited
        if node not in visited:
            visited.add(node)  # Mark it as visited

            # Add neighbors of the current node to the queue
            for neighbor in graph[node]:
                if neighbor not in visited:
                    queue.append(neighbor)

    # If we exhaust the queue without finding the goal, return None
    print(f"Goal '{goal}' not found.")
    return None

# Example usage:
start_node = 'A'
goal_node = 'G'

# Perform BFS to find the goal node
bfs(graph, start_node, goal_node)
