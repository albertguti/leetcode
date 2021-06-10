"""
128. Longest Consecutive Sequence
Medium

Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.

You must write an algorithm that runs in O(n) time.

 

Example 1:

Input: nums = [100,4,200,1,3,2]
Output: 4
Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.

Example 2:

Input: nums = [0,3,7,2,5,8,4,6,0,1]
Output: 9

 

Constraints:

    0 <= nums.length <= 105
    -109 <= nums[i] <= 109
"""
from typing import List

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums)
        longest = 0

        while nums_set:
            num = nums_set.pop()
            cnt = 1
            cnt += self.visitAdjacent(nums_set, num, 1)
            cnt += self.visitAdjacent(nums_set, num, -1)
            longest = max(longest, cnt)
        return longest
    
    def visitAdjacent(self, nums_set, num,  factor):
        following = num + factor
        cnt = 0
        while following in nums_set:
            nums_set.remove(following)
            following += factor
            cnt += 1
        return cnt
