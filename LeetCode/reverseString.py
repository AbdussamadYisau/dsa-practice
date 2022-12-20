# Time Complexity - O(N)
# Space Complexity - O(1)
class Solution:
    def reverseString(s):
        """
        Do not return anything, modify s in-place instead.
        """

        left = 0
        right = len(s) - 1

        while left < right:

            s[left], s[right] = s[right], s[left]

            left += 1
            right -= 1
        return s

print(Solution.reverseString(["h","e","l","l","o"]))