# Time Complexity - O(N)
# Space Complexity - O(1)

class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:

        i = 0
        j = 0

        while i < len(t):
            if j < len(s) and t[i] == s[j]:
                j += 1
            i += 1
        return j == len(s)

        
