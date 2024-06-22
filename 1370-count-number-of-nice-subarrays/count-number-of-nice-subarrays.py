class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        z=0
        start=0
        ans=0
        c=0
        for i in range(len(nums)):
            c+=nums[i]%2
            while start<i and (nums[start]%2==0 or c>k):
                if nums[start]%2:
                    z=0
                else:
                    z+=1
                c-=nums[start]%2
                start+=1
            if c==k:ans+=(z+1)
        return ans

def solve():
    f = open('user.out', 'w')
    iterator = map(loads, stdin)
    while True:
        try:
            nums = next(iterator)
            k = next(iterator)
        except StopIteration:
            break

        print(solution.numberOfSubarrays(nums, k), file=f)

solution = Solution()
solve()
exit()

"""
class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        for i in range(len(nums)):
            nums[i] %= 2
        
        prefix_count = [0] * (len(nums) + 1)
        prefix_count[0] = 1
        s = 0
        ans = 0
        
        for num in nums:
            s += num
            if s >= k:
                ans += prefix_count[s - k]
            prefix_count[s] += 1
        
        return ans
        
"""