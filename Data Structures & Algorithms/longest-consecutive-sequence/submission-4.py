class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hash = set(nums)
        longest = 0

        for x in nums:

            if x - 1 not in hash:
                current = x
                cnt = 1

                while current + 1 in hash:
                    current += 1
                    cnt+= 1
                
                longest = max(longest,cnt)

        return longest
