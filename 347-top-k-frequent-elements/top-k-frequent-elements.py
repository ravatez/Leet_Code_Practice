from collections import Counter
from heapq import nlargest

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = Counter(nums)

        top_k = nlargest(k, freq.keys(), key = freq.get)

        return top_k