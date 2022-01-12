"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

class Solution:
    """
    @param root: a TreeNode
    @return: a list of integer
    """
    def boundaryOfBinaryTree(self, root):
        # write your code here
        if not root: return []
        left_boundary = self.find_left_boundary(root.left)
        right_boundary = self.find_right_boundary(root.right)
        leaves = self.find_leaves(root)
        # print(leaves)

        if left_boundary and leaves and left_boundary[-1] == leaves[0]:
            left_boundary = left_boundary[:-1]
        if right_boundary and leaves and right_boundary[-1] == leaves[-1]:
            right_boundary = right_boundary[:-1]

        return [root.val] + left_boundary + leaves + right_boundary[::-1]

    def find_left_boundary(self, root):
        if not root: return []
        queue = collections.deque([root])
        res = []
        
        while queue:
            node = queue.popleft()
            # print(node.val)
            res.append(node.val)
            if node.left:
                queue.append(node.left)
            elif node.right:
                queue.append(node.right)
            else:
                return res
        
        return res
    
    def find_right_boundary(self, root):
        if not root: return []
        queue = collections.deque([root])
        res = []
        
        while queue:
            node = queue.popleft()
            # print(node.val)
            res.append(node.val)
            if node.right:
                queue.append(node.right)
            elif node.left:
                queue.append(node.left)
            else:
                return res
        
        return res

    ## use dfs by left most side 
    def find_leaves(self, root):
        if not root: return []
        path = [root]
        res = []
        
        while path:
            root = path.pop()
            if not root.right and not root.left:
                res.append(root.val)
            if root.right:
                path.append(root.right)
            if root.left:
                path.append(root.left)
        
        return res



#  1
#    \
#     2
#    / \
#   3   4

# left_boundary: []
# right_boundary: [2,4]
# leaves: []



#           1
#      /          \
#     2            3
#    / \          / 
#   4   5        6   
#      / \      / \
#     7   8    9  10  

# left_boundary: [2,4]
# right_boundary: [3,6,10]
# leaves: 
# queue = []
# res = [4,7,8,9,10]

# if left_boundary and leaves and left_boundary[-1] == leaves[0]: left_boundary = left_boundary[:-1]
# if right_boundary and leaves and right_boundary[-1] == leaves[-1]: right_boundary = right_boundary[:-1]

# [root.val] + left_boundary + leaves + right_boundary[::-1]


# {-8,-6,7,6,#,#,#,#,5}

#         -8
#         /  \
#     -6    7
#     / \. /. \
#     6  # #  #
#     / \
#     #. 5


# left_boundary: [-6,6,5]
# right_boundary: [7]
# leaves: [7,5]

# [-8] + [-6,6] + [5,7] + [7]