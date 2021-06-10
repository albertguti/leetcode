"""
784. Letter Case Permutation
Medium

Given a string s, we can transform every letter individually to be lowercase or uppercase to create another string.

Return a list of all possible strings we could create. You can return the output in any order.

 

Example 1:

Input: s = "a1b2"
Output: ["a1b2","a1B2","A1b2","A1B2"]

Example 2:

Input: s = "3z4"
Output: ["3z4","3Z4"]

Example 3:

Input: s = "12345"
Output: ["12345"]

Example 4:

Input: s = "0"
Output: ["0"]

 

Constraints:

    s will be a string with length between 1 and 12.
    s will consist only of letters or digits.
"""
from typing import List

class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        answer = []
        self.switchUpperLower(s, 0, answer)
        return answer
    
    def switchUpperLower(self, s, index, answer):
        if len(s) == index:
            answer.append(s)
            return
        char = s[index]
        if 'a' <= char <= 'z':
            string = s[:index] + char.upper() + s[index+1:]
            self.switchUpperLower(string, index+1, answer)
        elif 'A' <= char <= 'Z':
            string = s[:index] + char.lower() + s[index+1:]
            self.switchUpperLower(string, index+1, answer)
        self.switchUpperLower(s, index+1, answer)


obj = Solution()
res = obj.letterCasePermutation("a1b2")
print(res)