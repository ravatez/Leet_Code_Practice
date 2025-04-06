public class Solution {
    public IList<int> LargestDivisibleSubset(int[] nums) {
        int n = nums.Length;
        Array.Sort(nums);

        int[] dp = new int[n];    
        int[] prev = new int[n];   
        Array.Fill(dp, 1);
        Array.Fill(prev, -1);

        int maxIndex = 0;

        for (int i = 1; i < n; i++) {
            for (int j = 0; j < i; j++) {
                if (nums[i] % nums[j] == 0 && dp[j] + 1 > dp[i]) {
                    dp[i] = dp[j] + 1;
                    prev[i] = j;
                }
            }
            if (dp[i] > dp[maxIndex]) {
                maxIndex = i;
            }
        }

        List<int> result = new List<int>();
        int k = maxIndex;
        while (k != -1) {
            result.Add(nums[k]);
            k = prev[k];
        }

        result.Reverse(); 
        return result;
    }
}