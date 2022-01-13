# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        if not root: return 0
        self.max_difference = 0
        self.dfs(root)
        return self.max_difference
    
    def dfs(self, root):
        if not root: return sys.maxsize, -sys.maxsize ## 注意这里要返回系统允许的最大的min，和系统允许的最小的max， 不能return none or 0
        if not root.left and not root.right: return root.val, root.val
        
        left_min, left_max = self.dfs(root.left)
        right_min, right_max = self.dfs(root.right)
        
        running_max = max(root.val, left_max, right_max)
        running_min = min(root.val, left_min, right_min)
        # print(running_max, running_min)
        
        self.max_difference = max(self.max_difference, abs(root.val-running_max), abs(root.val-running_min))
        
        return running_min, running_max ## 注意对准min和max的顺序
    
    
    
#         8
#       /  \
#     3.   10
#   /   \      \
# 1      6.    14
#      /. \.    /
#     4.  7.   13
    
# self.max_difference: 7

# left_min: 1
# left_max: 7
# right_min: 10
# right_max: 14
    
# running_min: 1
# running_max: 14
    
# max(self.max_difference, |root.val - running_min|, |root.val - running_max|)
# Time: O(n) n: size of tree Space: O(1)