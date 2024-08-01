#O(n) prefix and postfix product
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        postfix = 1
        prefix = 1
        res = [0]*n
        for i in range(n):
            res[i] = prefix
            prefix *= nums[i]
        for i in range(n-1,-1,-1):
            res[i] *= postfix
            postfix *= nums[i]
        return res
