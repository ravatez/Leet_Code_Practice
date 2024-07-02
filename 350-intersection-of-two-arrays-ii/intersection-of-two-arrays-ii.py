class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        intersection = []
        nums1.sort()
        nums2.sort()
        i = 0
        for num in nums1:
            if i >= len(nums2):
                break
            while i < len(nums2) - 1 and nums2[i] < num:
                i += 1
            if nums2[i] == num:
                i += 1
                intersection.append(num)

        return intersection
#        return (Counter(nums1)&Counter(nums2)).elements()
"""
        nums1.sort()
        nums2.sort()
        
        i, j = 0, 0
        result = []
        
        while i < len(nums1) and j < len(nums2):
            if nums1[i] < nums2[j]:
                i += 1
            elif nums1[i] > nums2[j]:
                j += 1
            else:
                result.append(nums1[i])
                i += 1
                j += 1
                
        return result
"""