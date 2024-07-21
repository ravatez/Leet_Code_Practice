from collections import defaultdict
from graphlib import CycleError, TopologicalSorter

class Solution:
    def buildMatrix(self, k: int, rowConditions: List[List[int]], colConditions: List[List[int]]) -> List[List[int]]:
        def toposort(edges):
            pred = defaultdict(list)  # predecessors
            for x, y in edges:
                pred[y].append(x)
            ts = TopologicalSorter(pred)
            try:
                return list(ts.static_order())
            except CycleError:
                return []

        def fix_position(order):
            pos = {x: i for i, x in enumerate(order)}
            cur = len(order)
            for x in range(1, k + 1):
              if x not in pos:
                pos[x] = cur
                cur += 1
            return pos

        rowOrder = toposort(rowConditions)
        colOrder = toposort(colConditions)
        if not rowOrder or not colOrder:
            return []

        rowPos = fix_position(rowOrder)
        colPos = fix_position(colOrder)
        ans = [[0] * k for _ in range(k)]
        for x in range(1, k + 1):
            ans[rowPos[x]][colPos[x]] = x
        return ans