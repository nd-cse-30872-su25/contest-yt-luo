#!/usr/bin/env python3
def getmin(grid):
    m = len(grid)
    n = len(grid[0])
    dp = [[0 for _ in range(n)] for _ in range(m)]
    for j in range(n):
        for i in range(m):
            if j == 0:
                dp[i][j] = grid[i][j]
            else:
                if i == 0:
                    dp[i][j] = grid[i][j] + min(dp[m - 1][j - 1], dp[i + 1][j - 1], dp[i][j - 1])
                elif i == m - 1:
                    dp[i][j] = grid[i][j] + min(dp[0][j - 1], dp[i - 1][j - 1], dp[i][j - 1])
                else:
                    dp[i][j] = grid[i][j] + min(dp[i - 1][j - 1], dp[i + 1][j - 1], dp[i][j - 1])
    return dp

def get_path(dp):
    m, n = len(dp), len(dp[0])
    path = [0] * n

    # Step 1: Find min in last column
    min_row = 0
    for i in range(1, m):
        if dp[i][n - 1] < dp[min_row][n - 1]:
            min_row = i
    path[n - 1] = min_row

    # Step 2: Backtrack
    for j in range(n - 1, 0, -1):
        i = path[j]
        if i == 0:
            a, b, c = m - 1, 0, 1
        elif i == m - 1:
            a, b, c = m - 2, m - 1, 0
        else:
            a, b, c = i - 1, i, i + 1

        best_val = dp[a][j - 1]
        best_row = a
        if dp[b][j - 1] < best_val or (dp[b][j - 1] == best_val and b < best_row):
            best_val = dp[b][j - 1]
            best_row = b
        if dp[c][j - 1] < best_val or (dp[c][j - 1] == best_val and c < best_row):
            best_row = c

        path[j - 1] = best_row

    return [i + 1 for i in path]

# === MAIN PROGRAM ===
def main():
    import sys
    input_lines = sys.stdin.read().splitlines()
    idx = 0
    while idx < len(input_lines):
        if not input_lines[idx].strip():
            idx += 1
            continue
        m, n = map(int, input_lines[idx].strip().split())
        idx += 1
        grid = []
        for _ in range(m):
            row = list(map(int, input_lines[idx].strip().split()))
            grid.append(row)
            idx += 1

        dp = getmin(grid)
        cost = min(row[-1] for row in dp)
        path = get_path(dp)

        print(cost)
        print(' '.join(map(str, path)))

if __name__ == "__main__":
    main()

