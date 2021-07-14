"""
215. Kth Largest Element in an Array
Medium

Given an integer array nums and an integer k, return the kth largest element in the array.

Note that it is the kth largest element in the sorted order, not the kth distinct element.

 

Example 1:

Input: nums = [3,2,1,5,6,4], k = 2
Output: 5

Example 2:

Input: nums = [3,2,3,1,2,4,5,5,6], k = 4
Output: 4

 

Constraints:

    1 <= k <= nums.length <= 104
    -104 <= nums[i] <= 104
"""

from typing import List

from heapq import nlargest

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        return nlargest(k,nums)[-1]

from heapq import heappush, heappop
class SolutionHeapOptimised:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap =[]
        for num in nums:
            heappush(heap, num)
            if len(heap) > k:
                heappop(heap)
        print(heap)
        return(heappop(heap))



# Considered most optimal by leetcode
class Solution: 
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # nlogn: sort
        # basic sor
        # maintain size k heap --> n*logk
        # maintain size n heap --> n + klogn
        # quick select --> best O(n), worst O(n^2) 
        
        return self.quick_select(nums, len(nums)-k )
        
    
    def partition(self, nums, begin, end):
        pivot = begin
        for idx in range(begin+1, end+1):
            if nums[idx] <= nums[begin]:
                pivot += 1
                nums[idx], nums[pivot] = nums[pivot], nums[idx]
        nums[pivot], nums[begin] = nums[begin], nums[pivot]

        return pivot
    

    
    def quick_select(self, nums, k, begin=0, end=None):
        """return k smallest """
        
        if end is None:
            end = len(nums)-1

        pivot_idx = self.partition(nums, begin, end)

        if pivot_idx == k:
            return nums[pivot_idx]

        elif pivot_idx > k:
            return self.quick_select(nums, k, begin, pivot_idx-1)
        else:
            return self.quick_select(nums, k, pivot_idx+1 , end)










class SolutionQuickSelectRecursive:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        return self.quickSelect(nums, 0, len(nums) - 1, k)

    def quickSelect(self, nums: List[int], low: int, high: int, k: int):
        pivot = low

        for j in range(low, high):
            if nums[j] <= nums[high]:
                nums[pivot], nums[j] = nums[j], nums[pivot]
                pivot += 1
        nums[pivot], nums[high] = nums[high], nums[pivot]


        count = high - pivot + 1

        if (count == k):
            return nums[pivot]

        if (count > k):
            return self.quickSelect(nums, pivot + 1, high, k)

        return self.quickSelect(nums, low, pivot - 1, k - count)

class SolutionQuickSelectIterative:
    def findKthLargest(self, A: List[int], k: int) -> int:
        k = len(A) - k
        l = 0
        r = len(A) - 1
        while (l <= r):
            i = l
            for j in range(l+1, r+1):
                if (A[j] < A[l]):
                    i+=1
                    A[j],A[i] = A[i],A[j]
            A[l],A[i] = A[i],A[l]

            if (k < i):
                r = i - 1
            elif (k > i):
                l = i + 1
            else:
                return A[i]
        return -1; 