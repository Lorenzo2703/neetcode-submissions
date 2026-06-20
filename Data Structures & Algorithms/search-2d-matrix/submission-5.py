class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        n = len(matrix)
        m = len(matrix[0])

        top = 0
        bottom = n - 1
        left = 0
        right = m - 1

        while top <= bottom:
            mid = top +(bottom-top)//2

            if matrix[mid][0] <= target <= matrix[mid][-1]:
                while left <=right:
                    innerMid = left + (right-left)//2
                    if matrix[mid][innerMid] == target:
                        return True
                    elif matrix[mid][innerMid] < target:
                        left = innerMid + 1
                    else:
                        right = innerMid -1
                return False

            elif target < matrix[mid][0]:
                bottom = mid - 1
            else:
                top = mid + 1

                    
        return False
