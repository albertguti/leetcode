"""
55. Jump Game
Medium

Given an array of non-negative integers nums, you are initially positioned at the first index of the array.

Each element in the array represents your maximum jump length at that position.

Determine if you are able to reach the last index.

 
Example 1:

Input: nums = [2,3,1,1,4]
Output: true
Explanation: Jump 1 step from index 0 to 1, then 3 steps to the last index.

Example 2:

Input: nums = [3,2,1,0,4]
Output: false
Explanation: You will always arrive at index 3 no matter what. Its maximum jump length is 0, which makes it impossible to reach the last index.

 

Constraints:

    1 <= nums.length <= 3 * 10^4
    0 <= nums[i] <= 10^5
"""

from typing import List

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        fast = 0
        for i, num in enumerate(nums):
            if fast < i: # ens hem quedat enrere per no poder avançar
                return False
            fast = max(fast, num+i)
        return True

class SolutionBacktracking:
    def canJumpFromPosition(self, index, nums):
        if index == len(nums)-1:
            return True
        max_jump = min(nums[index] + index, len(nums)-1)
        for i in range(index+1, max_jump+1):
            if self.canJumpFromPosition(i, nums):
                return True
        return False

    def canJump(self, nums: List[int]) -> bool:
        return self.canJumpFromPosition(0, nums)


test_cases = [
    [[2,3,1,1,4], True],
    [[3,2,1,0,4], False]
]
obj = Solution()
for input, expected in test_cases:
    result = obj.canJump(input)
    print(result, expected)
    assert result == expected