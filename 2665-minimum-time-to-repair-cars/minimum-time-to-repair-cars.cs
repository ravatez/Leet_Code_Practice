public class Solution {
    public long RepairCars(int[] ranks, int cars) {
        long left = 1, right = (long)ranks.Min() * cars * cars;

        while (left < right) {
            long mid = (left + right) / 2;
            if (CanRepairAll(ranks, cars, mid)) {
                right = mid;
            } else {
                left = mid + 1;
            }
        }

        return left;
    }

    private bool CanRepairAll(int[] ranks, int cars, long time) {
        long totalCarsRepaired = 0;
        foreach (int rank in ranks) {
            totalCarsRepaired += (long)Math.Sqrt(time / rank);
            if (totalCarsRepaired >= cars) return true;
        }
        return false;
    }
}