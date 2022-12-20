class Solution:
    def moveZeroes(nums) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        prevIdx = 0

        for i in range(len(nums)):
            if nums[i] != 0:
                nums[prevIdx], nums[i] = nums[i], nums[prevIdx]
                prevIdx += 1

        print(nums)



print(Solution.moveZeroes([0,0,1]))