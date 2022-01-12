# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root: return False
        return self.find_next(root, targetSum)
        
        
    def find_next(self, root, target_sum):
        if not root: return False
        if not root.left and not root.right:
            if root.val == target_sum:
                return True
            
        if root.left: left_result = self.find_next(root.left, target_sum-root.val)
        if root.right: right_result = self.find_next(root.right, target_sum-root.val)
        
        if left_result or right_result:
            return True
        
        return False
    
#     targetSum: 22
#       5
#     /.  \
#    4     8
#  /      /. \
# 11.     13.  4
# / \           \
# 7. 2           1

# target_sum: 2
# Time: O(n)   Space: O(1)