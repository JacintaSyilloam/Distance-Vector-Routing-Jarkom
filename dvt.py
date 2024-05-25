class Graph:
    def __init__(self, vertices):
        self.V = vertices  # Number of vertices
        self.edges = []    # List of edges

    # function to add an edge to graph
    def add_edge(self, u, v, w):
        self.edges.append([u, v, w])

    def bellman_ford(self, start, end):
        # Step 1: Initialize distances from src to all other vertices
        # as INFINITE
        dist = {chr(97 + i): float("inf") for i in range(self.V)}
        dist[start] = 0

        # Initialize predecessors for path reconstruction
        predecessor = {chr(97 + i): None for i in range(self.V)}

        # Step 2: Relax all edges |V| - 1 times. A simple shortest
        # path from src to any other vertex can have at-most |V| - 1
        # edges
        for _ in range(self.V - 1):
            # Update dist value and parent index of the adjacent vertices of
            # the picked vertex. Consider only those vertices which are still in
            # queue
            for u, v, w in self.edges:
                if dist[u] != float("inf") and dist[u] + w < dist[v]:
                    dist[v] = dist[u] + w
                    predecessor[v] = u
        
        # Step 3: check for negative-weight cycles. The above step
        # guarantees shortest distances if graph doesn't contain
        # negative weight cycle. If we get a shorter path, then there
        # is a cycle.
        for u, v, w in self.edges:
            if dist[u] != float("inf") and dist[u] + w < dist[v]:
                print("Graph contains negative weight cycle")
                return

        # Print the calculated shortest distance
        if dist[end] == float("inf"):
            print(f"No path from {start} to {end}")
        else:
            print(f"\033[96mShortest distance from {start} to {end} is {dist[end]}\033[0m")
            self.print_path(predecessor, start, end)

    # utility function used to print the solution
    def print_path(self, predecessor, start, end):
        path = []
        current = end
        while current is not None:
            path.append(current)
            current = predecessor[current]
        path.reverse()
        print("Path taken:", " -> ".join(path))

def main():
    # Create a graph given in the above diagram
    g = Graph(12)
    g.add_edge('a', 'b', 4)
    g.add_edge('a', 'e', 10)
    g.add_edge('b', 'c', 13)
    g.add_edge('b', 'f', 2)
    g.add_edge('b', 'k', 11)
    g.add_edge('b', 'i', 7)
    g.add_edge('c', 'd', 9)
    g.add_edge('c', 'f', 6)
    g.add_edge('d', 'h', 15)
    g.add_edge('h', 'g', 4)
    g.add_edge('h', 'l', 15)
    g.add_edge('g', 'l', 7)
    g.add_edge('e', 'i', 14)
    g.add_edge('e', 'j', 6)
    g.add_edge('f', 'j', 11)
    g.add_edge('f', 'k', 5)
    g.add_edge('i', 'j', 6)
    g.add_edge('j', 'k', 3)
    g.add_edge('k', 'l', 11)

    # Take user input for start and end nodes
    print("\033[46mDistance Vector Routing\033[0m")
    start = input("Enter start node: ").strip()
    end = input("Enter end node: ").strip()

    # Check if the input nodes are valid
    if start not in 'abcdefghijkl' or end not in 'abcdefghijkl':
        print("Invalid input. Please enter nodes between 'a' and 'l'.")
        return

    # Run Bellman-Ford algorithm
    g.bellman_ford(start, end)

if __name__ == "__main__":
    main()
