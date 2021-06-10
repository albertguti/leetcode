"""
41. First Missing Positive
Hard

Given an unsorted integer array nums, find the smallest missing positive integer.

You must implement an algorithm that runs in O(n) time and uses constant extra space.

 

Example 1:

Input: nums = [1,2,0]
Output: 3

Example 2:

Input: nums = [3,4,-1,1]
Output: 2

Example 3:

Input: nums = [7,8,9,11,12]
Output: 1

 

Constraints:

    1 <= nums.length <= 5 * 105
    -231 <= nums[i] <= 231 - 1
"""

from typing import List

class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums)
        for i in range(n):
            num = nums[i] - 1
            while nums[i] != i+1 and 0 < nums[i] < n:
                tmp = nums[i]
                tmp2 = nums[nums[i] - 1]
                nums[i] = tmp2
                nums[tmp - 1] = tmp
        print(nums)
        for i, num in enumerate(nums):
            if i+1 != num:
                return i+1
                
        return n+1


obj = Solution()
res = obj.firstMissingPositive([3,4,-1,1])
print(res)