class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hash = set(nums)
        longest = 0

        for x in hash:

            if x - 1 not in hash:
                current = x
                count = 1

                while current + 1 in hash:
                    current += 1
                    count += 1

                longest = max(longest,count)
                
        return longest
            