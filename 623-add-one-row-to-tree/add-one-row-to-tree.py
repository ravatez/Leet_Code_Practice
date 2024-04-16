# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def addOneRow(self, root: Optional[TreeNode], v: int, d: int) -> Optional[TreeNode]:
        
        def dfs(node,depth,d):
            if not node: return None
            elif d==1:
                temp = TreeNode(v,left=node)
                return temp
            elif depth==d-1:
                node.left = TreeNode(v,left=node.left)
                node.right = TreeNode(v,right=node.right)
                return node
            dfs(node.left,depth+1,d)
            dfs(node.right,depth+1,d)
            return node
            
        return dfs(root,1,d)