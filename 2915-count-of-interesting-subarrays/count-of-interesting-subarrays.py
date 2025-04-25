class Solution:
    def countInterestingSubarrays(self, a: List[int], m: int, k: int) -> int:
        p = Counter({0:1})
        return sum((p[(q-k)%m],p.update([q%m]))[0] for q in accumulate(map(lambda v:v%m==k,a)))