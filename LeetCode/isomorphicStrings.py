'''
Time Complexity: O(N). We process each character in both the strings exactly once to determine if the strings are isomorphic.
Space Complexity: O(1) since the size of the ASCII character set is fixed and the keys in our dictionary are all valid ASCII characters according to the problem statement.

'''
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        sHashmap, tHashmap = {}, {}

        for i in range(len(s)):
            c1, c2 = s[i], t[i]

            if (c1 in sHashmap and sHashmap[c1] != c2) or (c2 in tHashmap and tHashmap[c2] != c1):
                return False

            sHashmap[c1] = c2
            tHashmap[c2] = c1

        return True

