class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        visit = set()
        perimeter = 0

        def dfs(i, j):
            nonlocal perimeter
            if i >= len(grid) or j >= len(grid[0]) or i < 0 or j < 0 or grid[i][j] == 0:
                return 1

            if (i, j) in visit:
                return 0

            visit.add((i, j))  # Marking the cell as visited

            prim = dfs(i, j + 1)
            prim += dfs(i + 1, j)
            prim += dfs(i, j - 1)
            prim += dfs(i - 1, j)

            perimeter += prim
            return prim

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]:
                    perimeter += dfs(i, j)

        return perimeter
