#Binary Search O(log n)
class Solution:
    def findMin(self, nums: List[int]) -> int:
        ans = nums[0] #init to index 0
        lp, rp = 0, len(nums)-1 #assign lp and rp

        while lp<=rp:
            if nums[lp]<nums[rp]: #if lp < rp compare nums[lp] with ans
                ans = min(ans, nums[lp])
            mid = (lp+rp)//2 #finding mid
            ans = min(ans, nums[mid]) #compare mid val and ans
            if nums[mid]>=nums[lp]: #if mid >= lp val, check right of mid
                lp = mid + 1
            else: #else check left of mid
                rp = mid - 1
        return ans
