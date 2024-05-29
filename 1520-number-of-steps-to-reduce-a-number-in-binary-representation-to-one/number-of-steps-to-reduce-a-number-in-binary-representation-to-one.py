class Solution:
    def numSteps(self, s: str) -> int:
        l = len(s)
        i = 1
        while s[l-i]=='0':
            i+=1
        return l+s.count('0')-i+2 if l!=i else l-1