class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        m = defaultdict(int)
        for n in nums:
            for i in range(32):
                m[i] += (n>>i) & 1

        res = 0

        for i in range(32):
            kth_bit = (k>>i) & 1

            if kth_bit == 1:
                if m[i]%2 == 0:
                    res += 1
            else:
                if m[i]%2 == 1:
                    res += 1
        return res
