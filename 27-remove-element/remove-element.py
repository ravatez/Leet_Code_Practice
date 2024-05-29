class Solution:
    def removeElement(self, num: List[int], val: int) -> int:
        index = 0
        for i in range(len(num)):
            if num[i] != val:
                num[index] = num[i]
                index += 1
        return index
