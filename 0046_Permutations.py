"""
46. Permutations
Medium

Given an array nums of distinct integers, return all the possible permutations. You can return the answer in any order.

 

Example 1:

Input: nums = [1,2,3]
Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]

Example 2:

Input: nums = [0,1]
Output: [[0,1],[1,0]]

Example 3:

Input: nums = [1]
Output: [[1]]

 

Constraints:

    1 <= nums.length <= 6
    -10 <= nums[i] <= 10
    All the integers of nums are unique.

"""

from dataclasses import List

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []
        n = len(nums)
        self.permutations(nums, 0, n-1 , result)
        return result
    
    def permutations(self, array, left, right, result):

        if left == right: # If we arrive to the end (the "right" is fixed)
            result.append(array[:])
        else:
            for i in range(left, right+1):
                array[left], array[i] = array[i], array[left] # Swap to find combinations
                self.permutations(array, left+1, right, result) # Fix the left part of the array and find next permutations
                array[left], array[i] = array[i], array[left] # Backtrack. We let the array as was for the previously stacked case