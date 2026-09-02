class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        low = 1
        high = max(piles)
        piles.sort()
        ans = 100000

        while low <= high:

            mid = (low+ high)//2
            
            totalTime = 0 
            for p in piles:
                totalTime += math.ceil(float(p)/mid)
            
            if totalTime <= h:
                ans = mid
                high = mid - 1
            else:
                low = mid + 1
        return ans
        









        