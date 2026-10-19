class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        hashMap = {}
        for i in range(0, len(nums)):
            bal = target - nums[i]
            if bal in hashMap:
                return [i, hashMap[bal]]
            hashMap[nums[i]] = i
        
        return [0,0]