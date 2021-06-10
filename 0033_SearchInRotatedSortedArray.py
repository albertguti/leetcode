"""
33. Search in Rotated Sorted Array
Medium

There is an integer array nums sorted in ascending order (with distinct values).

Prior to being passed to your function, nums is rotated at an unknown pivot index k (0 <= k < nums.length) such that the resulting array is [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-indexed). For example, [0,1,2,4,5,6,7] might be rotated at pivot index 3 and become [4,5,6,7,0,1,2].

Given the array nums after the rotation and an integer target, return the index of target if it is in nums, or -1 if it is not in nums.

You must write an algorithm with O(log n) runtime complexity.

 

Example 1:

Input: nums = [4,5,6,7,0,1,2], target = 0
Output: 4

Example 2:

Input: nums = [4,5,6,7,0,1,2], target = 3
Output: -1

Example 3:

Input: nums = [1], target = 0
Output: -1

 

Constraints:

    1 <= nums.length <= 5000
    -104 <= nums[i] <= 104
    All values of nums are unique.
    nums is guaranteed to be rotated at some pivot.
    -104 <= target <= 104
"""

class Solution:
    def search(self, nums, target):
        n = len(nums)
        left = 0
        right = n-1
        mid = (left+right)//2
        
        while left < right:
            mid = (left+right)//2
            if nums[mid] > nums[right]:
                left = mid+1 # Rebutgem l'element més gran
            else:
                right = mid
        rotate = left # L'element més petit sempre queda a l'esquerra
        
        left = 0
        right = n-1
        while left <= right:
            mid = (left+right)//2
            realmid = (mid+rotate)%n # Fer cerca binària normal però introduir aquesta rotació.
            if nums[realmid] == target:
                return realmid
            elif nums[realmid] < target:
                left = mid+1
            else:
                right = mid-1
        return -1

test_cases = [
    [[4,5,6,7,0,1,2], 0, 4],
    [[3,1],1,1]
]

obj = Solution()
for nums, target, expected in test_cases:
    result = obj.search(nums, target)
    assert result == expected