public class Solution {
    public long ColoredCells(int n) {
        return 1 + 4L * n * (n - 1) / 2;
    }
}