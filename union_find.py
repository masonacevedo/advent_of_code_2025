class UnionFind:
    """
    Union-Find (Disjoint Set Union) data structure for string elements.

    Supports near O(1) amortized union and find operations via:
      - Path compression
      - Union by rank
    """

    def __init__(self, elements: list[str]):
        """Initialize with a known list of string elements."""
        self.index = {e: i for i, e in enumerate(elements)}
        self.elements = elements  # index -> element reverse lookup
        self.parent = list(range(len(elements)))
        self.rank = [0] * len(elements)
        self.size = [1] * len(elements)
        self.num_components = len(elements)

    def _find(self, i: int) -> int:
        """Internal find by index with path compression."""
        if self.parent[i] != i:
            self.parent[i] = self._find(self.parent[i])
        return self.parent[i]

    def find(self, x: str) -> str:
        """Return the representative element of x's set."""
        return self.elements[self._find(self.index[x])]

    def union(self, x: str, y: str) -> bool:
        """
        Merge the sets containing x and y.
        Returns True if they were in different sets, False if already connected.
        """
        ix, iy = self._find(self.index[x]), self._find(self.index[y])
        if ix == iy:
            return False

        if self.rank[ix] < self.rank[iy]:
            ix, iy = iy, ix
        self.parent[iy] = ix
        self.size[ix] += self.size[iy]
        if self.rank[ix] == self.rank[iy]:
            self.rank[ix] += 1

        self.num_components -= 1
        return True

    def connected(self, x: str, y: str) -> bool:
        """Return True if x and y are in the same set."""
        return self._find(self.index[x]) == self._find(self.index[y])

    def component_count(self) -> int:
        """Return the number of disjoint sets."""
        return self.num_components

    def component_size(self, x: str) -> int:
        """Return the size of the component containing x. O(1) amortized."""
        return self.size[self._find(self.index[x])]

    def component_sizes(self) -> dict[str, int]:
        """Return a dict mapping each component's representative to its size. O(n)."""
        return {
            self.elements[i]: self.size[i]
            for i in range(len(self.elements))
            if self.parent[i] == i  # only roots
        }


# --- Example usage ---

if __name__ == "__main__":
    people = ["alice", "bob", "carol", "dave", "eve", "frank"]
    uf = UnionFind(people)
    print(f"Components: {uf.component_count()}")  # 6

    uf.union("alice", "bob")
    uf.union("bob", "carol")
    uf.union("dave", "eve")
    print(f"Components: {uf.component_count()}")  # 3

    print(f"alice and carol connected? {uf.connected('alice', 'carol')}")  # True
    print(f"alice and dave connected? {uf.connected('alice', 'dave')}")    # False

    uf.union("carol", "dave")
    print(f"alice and eve connected? {uf.connected('alice', 'eve')}")      # True
    print(f"Components: {uf.component_count()}")  # 2

    print(f"Representative of bob's set: {uf.find('bob')}")   # alice or carol (root)

    print(f"Size of alice's component: {uf.component_size('alice')}")  # 5
    print(f"Size of frank's component: {uf.component_size('frank')}")  # 1
    print(f"Component sizes: {uf.component_sizes()}")  # {root: 5, 'frank': 1}