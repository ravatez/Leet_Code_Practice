public class Solution {
    public int[] FindMissingAndRepeatedValues(int[][] grid) {
        int n = grid.Length;
        int size = n * n;
        int[] count = new int[size + 1];

        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                count[grid[i][j]]++;
            }
        }

        var (a, b) = (-1, -1);

        for (int num = 1; num <= size; num++) {
            if (count[num] == 2) {
                a = num;
            } else if (count[num] == 0) {
                b = num;
            }
        }

        return new int[] { a, b };
    }
}