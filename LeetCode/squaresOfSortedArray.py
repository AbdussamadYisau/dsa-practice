# Time Complexity - O(N)
# Space Complexity - O(N)
class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        i = 0
        j = len(nums) - 1
        ans = []

        while i <= j:
            if abs(nums[i]) > abs(nums[j]):
                ans.append(abs(nums[i]) * abs(nums[i]))
                i += 1
            else:
                ans.append(abs(nums[j]) * abs(nums[j]))
                j -= 1

        return ans[::-1]