class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:
        return (nums:=list(accumulate(nums))) and sum(2*x>=nums[-1] for x in nums[0:-1])