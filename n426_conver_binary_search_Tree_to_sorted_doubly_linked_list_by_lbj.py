"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

class Solution:
    """
    @param root: root of a tree
    @return: head node of a doubly linked list
    """
    def treeToDoublyList(self, root):
        # Write your code here.
        if not root: return None
        head, tail = self.in_order(root)

        head.left = tail
        tail.right = head
        return head

    def in_order(self, root):
        if not root: return None, None
        if not root.left and not root.right: return root, root

        left_head, left_tail = self.in_order(root.left)
        right_head, right_tail = self.in_order(root.right)

        if left_tail:
            left_tail.right = root
            root.left = left_tail
        if right_head:
            right_head.left = root
            root.right = right_head

        return left_head or root, right_tail or root


#         4
#        /  \
#       2   5
#      / \
#     1   3

# left_subtree - root - right_subtree

# root: 4

# left_head: 1
# left_tail: 3

# right_head: 5
# right_tail: 5

# left_tail.right = root
# root.left ...
# right_head.left = root
# root.right ...

# head: 1
# tail: 5

# tail + head .... tail + head

# 1 <-> 2 <-> 3 <-> 4 <-> 5
# <----------------------->
# Time: O(n) n: size of tree Space: O(1)