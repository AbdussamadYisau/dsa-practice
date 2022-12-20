# Time Complexity - O(N)
# Space Complexity - O(n)

'''
In the loop, you are going through each word in input S.

So let’s say there are K words (after splitting) each with average length L

we are running the outer loop K times. 
Within each iteration, we are doing L amount of work by doing [::-1] 

K*L = N, where N is the size of input string, s

'''
class Solution:
    def reverseWords(self, s: str) -> str:

        string_array = s.split(" ")


        for i in range(len(string_array)):

            string_array[i] = string_array[i][::-1]

        return " ".join(string_array)






