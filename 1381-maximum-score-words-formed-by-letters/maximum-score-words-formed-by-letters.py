class Solution:
    def maxScoreWords(self, w: List[str], l: List[str], s: List[int]) -> int:
        return (f:=lambda i,l:w[i:] and max(f(i+1,l),(q:=Counter(w[i]))<=l and sum(s[ord(c)-97]*q[c] for c in q)+f(i+1,l-q)) or 0)(0,Counter(l))