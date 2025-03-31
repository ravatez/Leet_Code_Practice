public class Solution {
    public long PutMarbles(int[] weights, int k) {
        if (k == 1) {
            return 0;
        }

        int[] pairSums = new int[weights.Length - 1];
        for (int i = 0; i < weights.Length - 1; i++) {
            pairSums[i] = weights[i] + weights[i + 1];
        }

        Array.Sort(pairSums);

        long minScore = 0, maxScore = 0;
        for (int i = 0; i < k - 1; i++) {
            minScore += pairSums[i];
            maxScore += pairSums[pairSums.Length - 1 - i];
        }

        return maxScore - minScore;
    }
}