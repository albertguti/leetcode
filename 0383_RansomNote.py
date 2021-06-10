"""
383. Ransom Note
Easy

Given two stings ransomNote and magazine, return true if ransomNote can be constructed from magazine and false otherwise.

Each letter in magazine can only be used once in ransomNote.

 

Example 1:

Input: ransomNote = "a", magazine = "b"
Output: false

Example 2:

Input: ransomNote = "aa", magazine = "ab"
Output: false

Example 3:

Input: ransomNote = "aa", magazine = "aab"
Output: true

 

Constraints:

    1 <= ransomNote.length, magazine.length <= 105
    ransomNote and magazine consist of lowercase English letters.

"""
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        cntmagazine = {}
        for char in magazine:
            if char not in cntmagazine:
                cntmagazine[char] = 1
            else:
                cntmagazine[char] += 1
                
        for char in ransomNote:
            if char in cntmagazine:
                if cntmagazine[char] == 1:
                    cntmagazine.pop(char)
                else:
                    cntmagazine[char] -= 1
            else:
                return False
        return True

"""
from collections import Counter
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        count_ransom = Counter(ransomNote)
        count_magazine = Counter(magazine)
        return not count_ransom - count_magazine
"""

obj = Solution()
print(obj.canConstruct("a","b"))