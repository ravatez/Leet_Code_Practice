from functools import reduce
from operator import xor

class Solution:
    def xorAllNums(self, A, B):
        return (len(A) % 2 * reduce(xor, B)) ^ (len(B) % 2 * reduce(xor, A))