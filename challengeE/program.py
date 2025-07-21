import sys
from typing import List, Optional
from collections import deque

# Define the TreeNode class
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# Solution with your DFS logic
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        if not root:
            return []
        path = []
        p_sum = 0
        res = []
        target = targetSum
        def dfs(node):
            nonlocal path, p_sum, res, target
            if not node.left and not node.right:
                if p_sum + node.val == target:
                    res.append(path.copy() + [node.val])
                    return
            p_sum += node.val
            path.append(node.val)
            if node.left:
                dfs(node.left)
            if node.right:
                dfs(node.right)
            p_sum -= node.val
            path.pop()
        dfs(root)        
        return res

# Function to build binary tree from BFS array (0 = None)
def build_tree_bfs(data: List[int]) -> Optional[TreeNode]:
    if not data or data[0] == 0:
        return None

    nodes = [TreeNode(val) if val != 0 else None for val in data]
    for i in range(len(data)):
        if nodes[i] is not None:
            li = 2 * i + 1
            ri = 2 * i + 2
            if li < len(data):
                nodes[i].left = nodes[li]
            if ri < len(data):
                nodes[i].right = nodes[ri]
    return nodes[0]
def main():
    lines = [line.strip() for line in sys.stdin if line.strip()]
    for i in range(0, len(lines), 2):
        target = int(lines[i])
        bfs_data = list(map(int, lines[i+1].split()))
        root = build_tree_bfs(bfs_data)
        sol = Solution()
        paths = sol.pathSum(root, target)
        paths.sort()
        for path in paths:
            print(f"{target}: {', '.join(map(str, path))}")
if __name__ == "__main__":
    main()
