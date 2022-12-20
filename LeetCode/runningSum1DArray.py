#Time Complexity - O(N)
#Space Complexity - O(N)

class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        ans = [nums[0]]

        for i in range(1, len(nums)):
            ans.append(sum(nums[:i+1])) 

        return ans

# Time Complexity - O(N)
# Space Complexity - O(1)
class SolutionOne:
    def runningSum(self, nums: List[int]) -> List[int]:
        for i in range(1, len(nums)):
            nums[i] += nums[i - 1]
        return nums