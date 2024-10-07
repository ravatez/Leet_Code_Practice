class Solution:
    def minLength(self, s: str) -> int:
        n=len(s)
        if n<2: return n
        t=[]
        for c in s:
            if t and ((t[-1]=='A' and c=='B') or (t[-1]=='C' and c=='D')):
                t.pop()
            else:
                t.append(c)
        return len(t)
        
        