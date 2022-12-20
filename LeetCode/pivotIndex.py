# Time - O(N * k (for splicing ?))
class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            leftSum = sum(nums[:i])
            rightSum = sum(nums[i+1:])

            if i == 0 and rightSum == 0:
                return 0

            if leftSum == rightSum:
                return i
        return -1
# Time Complexity - O(N)
# Space Complexity - O(1)

class SolutionOne(object):
    def pivotIndex(self, nums):
        S = sum(nums)
        leftsum = 0
        for i, x in enumerate(nums):
            if leftsum == (S - leftsum - x):
                return i
            leftsum += x
        return -1