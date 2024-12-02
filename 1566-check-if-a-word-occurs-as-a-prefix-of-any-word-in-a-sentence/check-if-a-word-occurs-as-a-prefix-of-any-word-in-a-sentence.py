class Solution:
    def isPrefixOfWord(self, s: str, w: str) -> int:
        return next((i for i,t in enumerate(s.split(),1) if match(w,t)),-1)