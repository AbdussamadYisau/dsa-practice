# Time Complexoty - O(k)
# Space Complexity - O(1)
class Solution(object):
    def rotate(self, nums, k):
        k=k%len(nums)
        nums[:]=nums[len(nums)-k:]+nums[:len(nums)-k]

#Time Complexity - O(n * k) , n cause of insert 

class SolutionOne(object):
    def rotate(self, nums, k):
        while k != 0: 
            lastNum = nums.pop()
            nums.insert(0, lastNum)

