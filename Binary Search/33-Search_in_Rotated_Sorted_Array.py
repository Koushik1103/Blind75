#binary search O(log n)
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        lp, rp = 0, len(nums) - 1

        while lp <= rp:
            mid = (lp + rp) // 2
            if target == nums[mid]:
                return mid
            if nums[lp] <= nums[mid]:
                if target > nums[mid] or target < nums[lp]:
                    lp = mid + 1
                else:
                    rp = mid - 1
            else:
                if target < nums[mid] or target > nums[rp]:
                    rp = mid - 1
                else:
                    lp = mid + 1
        return -1
