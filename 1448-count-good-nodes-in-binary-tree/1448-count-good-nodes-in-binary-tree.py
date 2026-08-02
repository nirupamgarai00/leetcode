# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        num = 0

        def count(root,mx = float('-inf')):
            if root == None:
                return
            mx = max(mx,root.val)
            if mx == root.val:
                nonlocal num
                num +=1
            
            count(root.left,mx)
            count(root.right,mx)
        count(root)
        return num
            

        