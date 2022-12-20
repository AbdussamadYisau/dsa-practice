# Time Complexity - O(N)
# Space Complexity - O(1)
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:

        left = 0
        right = len(numbers) - 1

        while left < right:
            total = numbers[left] + numbers[right]

            if target == total:
                return [left + 1, right + 1]

            elif target > total :
                left += 1

            else: 
                right -= 1