class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        mod_k=[0]*k
        mod_k[0]=1
        prefix=0
        for x in nums:
            prefix=(prefix+x)%k
            if prefix<0: prefix+=k
            mod_k[prefix]+=1
        ans=0
        for n in mod_k:
            ans+=n*(n-1)//2
        return ans
