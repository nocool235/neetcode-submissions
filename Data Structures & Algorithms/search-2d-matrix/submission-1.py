class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        def bs(row, target):

            low = 0
            high = len(row) - 1

            while low <= high:
                mid =  (low + high)//2

                if row[mid] == target: return True

                if row[mid] > target:
                    high = mid - 1
                else:
                    low = mid + 1 
            return False


        for i in range(len(matrix)):
            if matrix[i][0] <= target <= matrix[i][len(matrix[0]) -1]:
                return bs(matrix[i], target)
        
        return False
        
        