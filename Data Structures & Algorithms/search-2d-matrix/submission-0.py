class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l, r = 0, len(matrix) * len(matrix[0]) - 1
        while l <= r:
            m = (l + r) // 2
            i = m // len(matrix[0])
            j = m % len(matrix[0])
            t = matrix[i][j]
            print(l, r, t)
            if t == target:
                return True
            elif t > target:
                r = m - 1
            else:
                l = m + 1
        return False