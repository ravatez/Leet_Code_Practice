class Solution:
    def longestIdealString(self, s: str, k: int) -> int:
        
        l = [0] * 128
        for c in s:
            i = ord(c)
            l[i] = max(l[i - k : i + k + 1]) + 1
        return max(l)
"""
        dp = [0] * 26
        for c in s:
            for prev in range(26):
                curr = ord(c) - ord('a') # 0 - 25
                longest = 1
                for prev in range(26):
                    if abs(curr - prev) <= k:
                        longest = max(longest, 1 + dp[prev])
                dp[curr] = max(dp[curr], longest)
        return max(dp)

        cache = {}
        def helper(i, prev):
            if i == len(s):
                return 0
            if (i, prev) in cache:
                return cache[(i, prev)]

            
            res = helper(i + 1, prev) # skip s[i]

            if  prev == "" or abs(ord(s[i]) - ord(prev)) <+ k:
                res = max(res, 1+ helper(i + 1, s[i])) # include s[i] 
            cache[(i, prev)] = res
            return res
        
        return helper(0, "")


Less Optimal
        n = len(s)
        dp = [0] * n  # Dynamic programming array to store lengths of ideal subsequences ending at each position
        max_length = 0  # Variable to keep track of the maximum length

        for i in range(n):
            max_length_ending_at_i = 1  # Minimum length is always 1 for each character
            for j in range(i - 1, -1, -1):
                if abs(ord(s[i]) - ord(s[j])) <= k:
                    max_length_ending_at_i = max(max_length_ending_at_i, dp[j] + 1)
            dp[i] = max_length_ending_at_i
            max_length = max(max_length, dp[i])

        return max_length       
"""

       

            
