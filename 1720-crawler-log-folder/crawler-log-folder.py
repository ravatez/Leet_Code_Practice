class Solution:
    def minOperations(self, logs: List[str]) -> int:
        return reduce(lambda depth, log: depth - 1 if log == "../" and depth > 0 else depth + 1 if log != "./" and log != "../" else depth, logs, 0)