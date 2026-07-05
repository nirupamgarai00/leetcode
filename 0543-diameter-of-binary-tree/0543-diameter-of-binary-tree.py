# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, r: Optional[TreeNode]) -> int:
        ans = [0]
        def solve(root):
            if root == None:
                return 0
            
            d1 = solve(root.left)
            d2 = solve(root.right)
            ans[0] = max(ans[0],d1+d2)

            return 1 + max(d1,d2)
        solve(r)
        return ans[0]
            
            
            

            
            

        