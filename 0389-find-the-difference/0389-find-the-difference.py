class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        c = [0]*26
        for i in s:
            c[ord(i)-ord('a')] +=1
        for i in t:
            c[ord(i)-ord('a')] -=1
        cnt = 0
        for i in range(26):
            if c[i] == -1:
                return chr(i+ord('a'))
