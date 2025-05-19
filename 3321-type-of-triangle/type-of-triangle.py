class Solution(object):
    def triangleType(self, nums):
        """
        :type nums: List[int]
        :rtype: str
        """
        a, b, c = nums[0], nums[1], nums[2]

        # Step 1: Check triangle inequality
        if a + b <= c or a + c <= b or b + c <= a:
            return "none"

        # Step 2: Count unique side lengths
        unique_sides = len(set([a, b, c]))

        # Step 3: Determine triangle type
        return "equilateral" if unique_sides == 1 else \
               "isosceles" if unique_sides == 2 else "scalene"