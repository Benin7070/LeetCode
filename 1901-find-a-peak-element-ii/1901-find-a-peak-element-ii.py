class Solution:
    def findPeakGrid(self, mat: List[List[int]]) -> List[int]:
        rows = len(mat)
        cols = len(mat[0])

        l = 0
        r = rows - 1

        while l <= r:
            mid = (l + r) // 2

            max_index = 0

            for i in range(1, cols):
                if mat[mid][i] > mat[mid][max_index]:
                    max_index = i


            curr = mat[mid][max_index]
            if mid > 0 and mat[mid - 1][max_index] > curr:
                r = mid - 1

            elif mid < rows - 1 and mat[mid + 1][max_index] > curr:
                l = mid + 1

            else:
                return [mid, max_index]