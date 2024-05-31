from collections import Counter
class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        count = Counter(nums)
        index = [num for num, freq in count.items() if freq == 1]
        return index
        