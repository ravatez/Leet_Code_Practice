class Solution:

    def maxDistance(self, position: List[int], m: int) -> int:

        def check(minmax):
            rem = m - 1
            lim = position[0] + minmax
            for p in position[1:]:
                if p >= lim:
                    rem -= 1
                    lim = p + minmax
            return rem <= 0

        position.sort()
        if m == 2:
            return position[-1] - position[0]
        low = 1
        high = (position[-1] - position[0]) // (m - 1)
        while low < high:
            mid = (low + high + 1) // 2
            if check(mid):
                low = mid
            else:
                high = mid -1
        return low    
"""
class Solution:
    def fn(self, p, m, mid):
        cnt = 1
        prev = p[0]
        for i in range(1, len(p)):
            if p[i] - prev >= mid:
                cnt += 1
                prev = p[i]
        return cnt >= m

    def maxDistance(self, p, m):
        p.sort()
        lo = 1
        hi = p[-1] - p[0]
        while hi - lo > 1:
            mid = (lo + hi) // 2
            if self.fn(p, m, mid):
                lo = mid
            else:
                hi = mid - 1
        if self.fn(p, m, hi):
            return hi
        return lo
"""