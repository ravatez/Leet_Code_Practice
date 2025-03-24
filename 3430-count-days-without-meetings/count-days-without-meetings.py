class Solution:
    def countDays(self, days: int, meetings: List[List[int]]) -> int:
        intervals = set()

        for meeting in meetings:
            start = meeting[0]
            end = meeting[1]
            intervals.add((start, end))
        
        intervals = sorted(intervals)
        
        merged_intervals = []
        for interval in intervals:
            if not merged_intervals or merged_intervals[-1][1] < interval[0] - 1:
                merged_intervals.append(list(interval))
            else:
                merged_intervals[-1][1] = max(merged_intervals[-1][1], interval[1])
        
        busy_days = 0
        for interval in merged_intervals:
            busy_days += interval[1] - interval[0] + 1
        
        free_days = days - busy_days
        
        return free_days