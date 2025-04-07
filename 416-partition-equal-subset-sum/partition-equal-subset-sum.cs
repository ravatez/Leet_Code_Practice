public class Solution {
    public bool CanPartition(int[] nums) {
        int totalSum = 0;
        foreach (int num in nums) {
            totalSum += num;
        }
        if (totalSum % 2 != 0) {
            return false;
        }

        int target = totalSum / 2;
        bool[] dp = new bool[target + 1];
        dp[0] = true; 
        foreach (int num in nums) {
            for (int j = target; j >= num; j--) {
                dp[j] = dp[j] || dp[j - num];
            }
        }

        return dp[target];
    }
}