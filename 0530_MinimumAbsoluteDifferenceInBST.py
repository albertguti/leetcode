"""
530. Minimum Absolute Difference in BST
Easy

Given the root of a Binary Search Tree (BST), return the minimum absolute difference between the values of any two different nodes in the tree.

 

Example 1:

Input: root = [4,2,6,1,3]
Output: 1

Example 2:

Input: root = [1,0,48,null,null,12,49]
Output: 1

 

Constraints:

    The number of nodes in the tree is in the range [2, 104].
    0 <= Node.val <= 105
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    prev = float("-inf")
    ans = float("inf")
    def minDiffInBST(self, root: TreeNode) -> int:
        if not root:
            return
        self.minDiffInBST(root.left)
        self.ans = min(self.ans, root.val-self.prev)
        self.prev = root.val
        self.minDiffInBST(root.right)
        return self.ans



class SolutionSpaceOn: # Requires a new list. O(n) spatial complexity
    def getMinimumDifference(self, root: TreeNode) -> int:
        values = []
        self.visitInorder(root, values)
        min_diff = float("inf")
        for x,y in zip(values[:-1],values[1:]):
            diff = y-x
            min_diff = min(min_diff, diff)
        return min_diff
    
    def visitInorder(self, root, values):
        if root.left:
            self.visitInorder(root.left, values)
        values.append(root.val)
        if root.right:
            self.visitInorder(root.right, values)