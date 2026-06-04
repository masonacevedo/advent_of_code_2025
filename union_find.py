class UnionFind:
    """
    Union-Find (Disjoint Set Union) data structure.

    Supports near O(1) amortized union and find operations via:
      - Path compression
      - Union by rank
    """

    def __init__(self, n: int):
        """Initialize with n elements (0 to n-1), each in its own set."""
        self.parent = list(range(n))
        self.rank = [0] * n
        self.num_components = n

    def find(self, x: int) -> int:
        """Return the representative (root) of x's set."""
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])  # Path compression
        return self.parent[x]

    def union(self, x: int, y: int) -> bool:
        """
        Merge the sets containing x and y.
        Returns True if they were in different sets, False if already connected.
        """
        rx, ry = self.find(x), self.find(y)
        if rx == ry:
            return False  # Already in the same set

        # Union by rank: attach smaller tree under larger tree
        if self.rank[rx] < self.rank[ry]:
            rx, ry = ry, rx
        self.parent[ry] = rx
        if self.rank[rx] == self.rank[ry]:
            self.rank[rx] += 1

        self.num_components -= 1
        return True

    def connected(self, x: int, y: int) -> bool:
        """Return True if x and y are in the same set."""
        return self.find(x) == self.find(y)

    def component_count(self) -> int:
        """Return the number of disjoint sets."""
        return self.num_components


# --- Example usage ---

if __name__ == "__main__":
    uf = UnionFind(6)  # Elements: 0, 1, 2, 3, 4, 5
    print(f"Components: {uf.component_count()}")  # 6

    uf.union(0, 1)
    uf.union(1, 2)
    uf.union(3, 4)
    print(f"Components: {uf.component_count()}")  # 3

    print(f"0 and 2 connected? {uf.connected(0, 2)}")  # True
    print(f"0 and 3 connected? {uf.connected(0, 3)}")  # False

    uf.union(2, 3)
    print(f"0 and 4 connected? {uf.connected(0, 4)}")  # True
    print(f"Components: {uf.component_count()}")  # 2