class Graph:
    def __init__(self, vertices):
        self.V = vertices  # jumlah node
        self.edges = []    # List edges

    # function untuk menambahkan edge ke graph
    def add_edge(self, u, v, w):
        self.edges.append([u, v, w])
        self.edges.append([v, u, w])

    def bellman_ford(self, start, end):
        # Step 1: Inisialisasi jarak dari source ke semua node lainnya sebagai INFINITE
        dist = {chr(97 + i): float("inf") for i in range(self.V)}
        dist[start] = 0

        # Inisialisasi pendahulunya untuk rekonstruksi jalur
        predecessor = {chr(97 + i): None for i in range(self.V)}

        # Step 2: Relax semua edge |V| - 1 kali.
        # Jalur terpendek sederhana dari source ke node lain mana pun dapat memiliki paling banyak |V| - 1 edge
        for _ in range(self.V - 1):
            # Update jarak dan indeks parent yang berdekatan dari node yang dipilih
            # Pertimbangkan hanya node yang masih dalam antrian
            for u, v, w in self.edges:
                if dist[u] != float("inf") and dist[u] + w < dist[v]:
                    dist[v] = dist[u] + w
                    predecessor[v] = u
        
        # Step 3: Periksa siklus pada bobot negatif.
        # Langkah di atas menjamin jarak terpendek jika graph tidak mengandung siklus berbobot negatif.
        # JIka mendapatkan jalur terpendek, maka siklus terjadi
        for u, v, w in self.edges:
            if dist[u] != float("inf") and dist[u] + w < dist[v]:
                print("Graph contains negative weight cycle")
                return

        # Print jarak terpendek 
        if dist[end] == float("inf"):
            print(f"No path from {start} to {end}")
        else:
            print(f"\033[96mShortest distance from {start} to {end} is {dist[end]}\033[0m")
            self.print_path(predecessor, start, end)

    # utility function untuk print jalur yang dilalui untuk mendapatkan jalur terpendek
    def print_path(self, predecessor, start, end):
        path = []
        current = end
        while current is not None:
            path.append(current)
            current = predecessor[current]
        path.reverse()
        print("Path taken:", " -> ".join(path))

def main():
    # Buat graph sesuai dengan diagram yang dibuat
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

    # Ambil input user untuk start dan end node
    print("\033[46mDistance Vector Routing\033[0m")
    start = input("Enter start node: ").strip()
    end = input("Enter end node: ").strip()

    # Cek apabila input user valid
    if start not in 'abcdefghijkl' or end not in 'abcdefghijkl':
        print("Invalid input. Please enter nodes between 'a' and 'l'.")
        return

    # Jalankan Bellman-Ford algorithm
    g.bellman_ford(start, end)

if __name__ == "__main__":
    main()
