# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        if not root: return []
        self.result = []
        self.find_next(root, targetSum, [root.val])
        return self.result
        
        
    def find_next(self, root, target_sum, path):
        if not root: return
        if not root.left and not root.right:
            if root.val == target_sum:
                self.result.append(path[:]) # or list(path)
                return
        
        if root.left:
            path.append(root.left.val)
            # self.find_next(root.left, target_sum-root.val, path+[root.left.val])
            self.find_next(root.left, target_sum-root.val, path)
            path.pop()
        if root.right:
            path.append(root.right.val)
            # self.find_next(root.right, target_sum-root.val, path+[root.right.val])
            self.find_next(root.right, target_sum-root.val, path)
            path.pop()

            
#     targetSum: 22
#       5
#     /.  \
#    4     8
#  /      /. \
# 11.     13.  4
# / \         / \
# 7. 2       5   1    

# target_sum: 5
# path: [5, 8, 4, ]
# self.result: [[5, 4, 11, 2],[5, 8, 4, 5]]
# Time: O(n) n: size of tree Space: O(m) m: max depth of the tree