"""
414. Third Maximum Number
Easy

1035

1769

Add to List

Share
Given integer array nums, return the third maximum number in this array. If the third maximum does not exist, return the maximum number.

 

Example 1:

Input: nums = [3,2,1]
Output: 1
Explanation: The third maximum is 1.
Example 2:

Input: nums = [1,2]
Output: 2
Explanation: The third maximum does not exist, so the maximum (2) is returned instead.
Example 3:

Input: nums = [2,2,3,1]
Output: 1
Explanation: Note that the third maximum here means the third maximum distinct number.
Both numbers with value 2 are both considered as second maximum.
 

Constraints:

1 <= nums.length <= 104
-231 <= nums[i] <= 231 - 1
"""
from typing import List

class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        top3 = [float("-inf")]*3
        
        for num in nums:
            if num > top3[0]:
                top3 = [num, top3[0], top3[1]]
            elif top3[0] > num > top3[1]:
                top3 = [top3[0], num, top3[1]]
            elif top3[1] > num > top3[2]:
                top3 = [top3[0], top3[1], num]
        if float("-inf") in top3:
            return top3[0]
        return top3[-1]

test_cases = [
    [[2,2,3], 3]
]