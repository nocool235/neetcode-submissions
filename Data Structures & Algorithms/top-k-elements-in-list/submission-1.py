class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}

        for x in nums:
            count[x] = count.get(x,0) + 1

        heap = []
        
        for n,c in count.items():
            heapq.heappush(heap, (c,n))

            if len(heap) > k:
                heapq.heappop(heap)
        
        return[num for nums, num in heap]