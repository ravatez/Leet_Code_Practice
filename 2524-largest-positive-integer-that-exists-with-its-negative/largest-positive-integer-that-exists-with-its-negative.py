class Solution:
    def findMaxK(self, nums: List[int]) -> int:
        num_set = set(nums)
        max_k = -1
        
        for num in num_set:
            if num > 0 and -num in num_set:
                max_k = max(max_k, num)
        
        return max_k