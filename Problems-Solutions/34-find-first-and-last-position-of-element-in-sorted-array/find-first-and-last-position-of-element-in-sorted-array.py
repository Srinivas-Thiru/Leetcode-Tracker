class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        return [self.bfsHelper(nums, target, True), self.bfsHelper(nums, target, False)]
    
    def bfsHelper(self, nums, target, leftBiased):
            l, r = 0, len(nums)-1
            ans = -1
            while l <= r:
                mid = (l + r) // 2
                val = nums[mid]
                if val < target:
                    l = mid + 1
                if val > target:
                    r = mid - 1
                if val == target:
                    ans = mid
                    if leftBiased:
                        r = mid - 1
                    else:
                        l = mid + 1
            return ans