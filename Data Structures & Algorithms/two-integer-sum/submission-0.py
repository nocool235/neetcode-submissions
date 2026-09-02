class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        hash = {}

        for i in range(len(nums)):
            compliment = target - nums[i]

            if compliment in hash:
                return [hash[compliment], i]
            
            hash[nums[i]] = i
        