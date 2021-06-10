"""
3. Longest Substring Without Repeating Characters
Medium

Given a string s, find the length of the longest substring without repeating characters.

 

Example 1:

Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.

Example 2:

Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.

Example 3:

Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.

Example 4:

Input: s = ""
Output: 0

 

Constraints:

    0 <= s.length <= 5 * 104
    s consists of English letters, digits, symbols and spaces.
"""

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        visited = {}
        left = -1
        ans = 0
        for right, char in enumerate(s):
            left = max(visited.get(char, left), left) # No moure l'esquerra cap enrere
            ans = max(ans, right-left)
            visited[char] = right
        return ans

test_cases = [
    ["abba", 2],
    ["nnnnnn", 1],
    ["abcde", 5],
    ["abababc", 3]
]

obj = Solution()
for string, expected in test_cases:
    result = obj.lengthOfLongestSubstring(string)
    try:
        assert result == expected
    except AssertionError:
        print(f"Got {result}, expected {expected}")

print("Done")