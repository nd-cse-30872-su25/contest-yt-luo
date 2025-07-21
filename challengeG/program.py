#!/usr/bin/env python3

import sys

class DSU:
    def __init__(self, n):
        # -1 means “i is a root”
        self.parent = [-1] * n

    def find(self, x):
        if self.parent[x] < 0:
            return x
        self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        xr = self.find(x)
        yr = self.find(y)
        if xr == yr:
            return
        # attach y’s root to x’s root
        self.parent[yr] = xr

def count_circuits(matrix):
    n = len(matrix)
    dsu = DSU(n)
    for i in range(n):
        for j in range(i + 1, n):
            if matrix[i][j]:
                dsu.union(i, j)
    count = 0
    for p in dsu.parent:
        if p == -1:
            count += 1
    return count

def main():
    tokens = sys.stdin.read().split()
    idx = 0
    system = 1

    while idx < len(tokens):
        # read size
        n = int(tokens[idx])
        idx += 1

        # read adjacency matrix
        matrix = []
        for _ in range(n):
            row = list(map(int, tokens[idx:idx+n]))
            idx += n
            matrix.append(row)

        # compute and print result
        num = count_circuits(matrix)
        print(f"System {system} isolated circuits: {num}")
        system += 1

if __name__ == "__main__":
    main()
