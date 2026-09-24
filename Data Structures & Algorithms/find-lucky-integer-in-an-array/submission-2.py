from typing import List

class Solution:
    def findLucky(self, arr: List[int]) -> int:
        freq = {}

        largest  = -1 

        for x in arr:
            freq[x] = freq.get(x,0) + 1

        for x in arr:
            if x == freq[x]:
                largest = max(largest,x)
        
            
        return largest
            

        