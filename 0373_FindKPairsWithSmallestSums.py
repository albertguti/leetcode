"""
373. Find K Pairs with Smallest Sums
Medium

You are given two integer arrays nums1 and nums2 sorted in ascending order and an integer k.

Define a pair (u, v) which consists of one element from the first array and one element from the second array.

Return the k pairs (u1, v1), (u2, v2), ..., (uk, vk) with the smallest sums.

 

Example 1:

Input: nums1 = [1,7,11], nums2 = [2,4,6], k = 3
Output: [[1,2],[1,4],[1,6]]
Explanation: The first 3 pairs are returned from the sequence: [1,2],[1,4],[1,6],[7,2],[7,4],[11,2],[7,6],[11,4],[11,6]

Example 2:

Input: nums1 = [1,1,2], nums2 = [1,2,3], k = 2
Output: [[1,1],[1,1]]
Explanation: The first 2 pairs are returned from the sequence: [1,1],[1,1],[1,2],[2,1],[1,2],[2,2],[1,3],[1,3],[2,3]

Example 3:

Input: nums1 = [1,2], nums2 = [3], k = 3
Output: [[1,3],[2,3]]
Explanation: All possible pairs are returned from the sequence: [1,3],[2,3]

 

Constraints:

    1 <= nums1.length, nums2.length <= 104
    -109 <= nums1[i], nums2[i] <= 109
    nums1 and nums2 both are sorted in ascending order.
    1 <= k <= 1000
"""

from heapq import *
class Solution:

    def kSmallestPairs(self, nums1, nums2, k):

        if not nums1 or not nums2:
            return []

        visited = []
        heap = []
        output = []

        heappush(heap, (nums1[0] + nums2[0], 0, 0))
        visited.append((0, 0))

        while len(output) < k and heap:

            val = heappop(heap)
            output.append((nums1[val[1]], nums2[val[2]]))

            if val[1] + 1 < len(nums1) and (val[1] + 1, val[2]) not in visited:
                heappush(heap, (nums1[val[1] + 1] + nums2[val[2]], val[1] + 1, val[2]))
                visited.append((val[1] + 1, val[2]))

            if val[2] + 1 < len(nums2) and (val[1], val[2] + 1) not in visited:
                heappush(heap, (nums1[val[1]] + nums2[val[2] + 1], val[1], val[2] + 1))
                visited.append((val[1], val[2] + 1))

        return output

test_cases = [
    [[1,7,11], [2,4,6], 3, [[1,2],[1,4],[1,6]]],
    [[1,1,2], [1,2,3], 2, [[1,1],[1,1]]]
]

obj = Solution()
for nums1, nums2, k, expected in test_cases:
    result = obj.kSmallestPairs(nums1, nums2, k)
    print(result)
