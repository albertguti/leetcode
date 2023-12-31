"""
145. Binary Tree Postorder Traversal
Easy

Given the root of a binary tree, return the postorder traversal of its nodes' values.

 

Example 1:

Input: root = [1,null,2,3]
Output: [3,2,1]

Example 2:

Input: root = []
Output: []

Example 3:

Input: root = [1]
Output: [1]

Example 4:

Input: root = [1,2]
Output: [2,1]

Example 5:

Input: root = [1,null,2]
Output: [2,1]

 

Constraints:

    The number of the nodes in the tree is in the range [0, 100].
    -100 <= Node.val <= 100
"""
from typing import List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        values = []
        self.__postorderTraversalHelper(root, values)
        return values
    
    def __postorderTraversalHelper(self, root, values):
        if not root:
            return
        self.__postorderTraversalHelper(root.left, values)
        self.__postorderTraversalHelper(root.right, values)
        values.append(root.val)
