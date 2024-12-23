class Solution:
    def minSwapsToSort(self, arr):
        n = len(arr)
        indexedArr = [(arr[i], i) for i in range(n)]
        indexedArr.sort()
        visited = [False] * n
        swaps = 0

        for i in range(n):
            if visited[i] or indexedArr[i][1] == i:
                continue

            cycleSize = 0
            j = i
            while not visited[j]:
                visited[j] = True
                j = indexedArr[j][1]
                cycleSize += 1

            if cycleSize > 1:
                swaps += cycleSize - 1

        return swaps

    def minimumOperations(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        queue = [root]
        operations = 0

        while queue:
            levelSize = len(queue)
            level = []

            for _ in range(levelSize):
                node = queue.pop(0)
                level.append(node.val)

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            operations += self.minSwapsToSort(level)

        return operations