# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countPairs(self, root: TreeNode, distance: int) -> int:
        self.res = 0

        def solve(root):
            if root is None:
                return {}
            if root.left is None and root.right is None:
                # leaf node here
                return {1: 1}
            lhNodes = solve(root.left)            
            rhNodes = solve(root.right)
            
            for leftNodeHeight in lhNodes:
                for rightNodeHeight in rhNodes:
                    if leftNodeHeight + rightNodeHeight <= distance:
                        self.res += lhNodes[leftNodeHeight] * rhNodes[rightNodeHeight]

            nhNodes = {}
            for key in lhNodes:
                if key <= distance:
                    nhNodes[key + 1] = lhNodes[key]
            for key in rhNodes:
                if key <= distance:
                    nhNodes[key + 1] = nhNodes.get(key + 1, 0) + rhNodes[key]                    



            return nhNodes

        solve(root)
        return self.res

"""
class Solution:
    def countPairs(self, root: TreeNode, distance: int) -> int:
        self.map = {}
        self.leaves = []
        self.findLeaves(root, [], self.leaves, self.map)
        res = 0
        for i in range(len(self.leaves)):
            for j in range(i + 1, len(self.leaves)):
                list_i, list_j = self.map[self.leaves[i]], self.map[self.leaves[j]]
                for k in range(min(len(list_i), len(list_j))):
                    if list_i[k] != list_j[k]:
                        dist = len(list_i) - k + len(list_j) - k
                        if dist <= distance:
                            res += 1
                        break
        return res

    def findLeaves(self, node: TreeNode, trail: List[TreeNode], leaves: List[TreeNode], map: Dict[TreeNode, List[TreeNode]]):
        if not node:
            return
        tmp = trail[:]
        tmp.append(node)
        if not node.left and not node.right:
            map[node] = tmp
            leaves.append(node)
            return
        self.findLeaves(node.left, tmp, leaves, map)
        self.findLeaves(node.right, tmp, leaves, map)
"""