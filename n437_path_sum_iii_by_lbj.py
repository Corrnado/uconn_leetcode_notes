# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# BFS遍历全树 + DFS寻找合格的path
# 速度比较慢，时间是O(n^2)，空间是O(n)
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        if not root: return 0
        queue = collections.deque([root])
        self.result = 0
        while queue:
            current = queue.popleft()
            if not current: continue
            
            self.find_next(current, targetSum)
            queue.append(current.left)
            queue.append(current.right)
        return self.result
        
        
    def find_next(self, root, target_sum):
        if not root: return
        if root.val == target_sum:
            # print(root.val)
            self.result += 1
        
        if root.left:
            self.find_next(root.left, target_sum-root.val)
        if root.right:
            self.find_next(root.right, target_sum-root.val)


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# 用prefixsum来寻找合格的path，速度比较快，时间为O(n)，空间为O(n)
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        if not root: return 0
        self.count = 0
        seen = collections.defaultdict(int)
        seen[0] = 1
        self.dfs_pathSum(root, 0, seen, targetSum)
        
        return self.count
    
    def dfs_pathSum(self, root, curSum, seen, target):
        if not root:
            return
        curSum += root.val
        
        if curSum - target in seen:
            self.count += seen[curSum-target]
            
        seen[curSum] += 1        
        self.dfs_pathSum(root.left, curSum, seen, target)
        self.dfs_pathSum(root.right, curSum, seen, target)        
        seen[curSum] -= 1