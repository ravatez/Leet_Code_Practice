class Solution:
    def passThePillow(self, n: int, time: int) -> int:
        left_to_right = True
        pos = 1
        for i in range(1, time+1):
            if left_to_right:
                pos += 1
            else:
                pos -= 1
            if i%(n-1) == 0:
                left_to_right = not left_to_right
        return pos

""" 
        chunks = time // (n - 1)
        return (time % (n - 1) + 1) if chunks % 2 == 0 else (n - time % (n - 1))   
"""