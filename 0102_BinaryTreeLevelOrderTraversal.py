"""
Given the root of a binary tree, return the level order traversal of its nodes' values. (i.e., from left to right, level by level).

 

Example 1:

Input: root = [3,9,20,null,null,15,7]
Output: [[3],[9,20],[15,7]]

Example 2:

Input: root = [1]
Output: [[1]]

Example 3:

Input: root = []
Output: []

 

Constraints:

    The number of nodes in the tree is in the range [0, 2000].
    -1000 <= Node.val <= 1000
"""
from typing import List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        ans = []
        unvisited = [root]
        is_level = True
        tmp = []
        while unvisited and is_level:
            tmpunvisited = []
            is_level = False
            for node in unvisited:
                if node is None:
                    tmp.append(None)
                    tmpunvisited.append(None)
                    tmpunvisited.append(None)
                else:
                    tmp.append(node.val)
                    tmpunvisited.append(node.left)
                    tmpunvisited.append(node.right)
                    is_level = True
            unvisited  = tmpunvisited[:]
            ans.append(tmp)
        return ans

tree = TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))
obj = Solution()
result = obj.levelOrder(tree)
print(result)