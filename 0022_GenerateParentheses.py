"""
22. Generate Parentheses
Medium

Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

Example 1:

Input: n = 3
Output: ["((()))","(()())","(())()","()(())","()()()"]

Example 2:

Input: n = 1
Output: ["()"]

 

Constraints:

    1 <= n <= 8
"""
from typing import List
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        parentheses = []
        self.generateCombinations(n, n, parentheses, "")
        return parentheses
    
    def generateCombinations(self, left, right, answer, combination):
        if left == 0 and right == 0:
            answer.append(combination)
            return
        if 0 <= left < right:
            self.generateCombinations(left, right-1, answer, combination + ")")
        if 0 < left:
            self.generateCombinations(left-1, right, answer, combination + "(")

obj = Solution()
res = obj.generateParenthesis(3)
print(res)