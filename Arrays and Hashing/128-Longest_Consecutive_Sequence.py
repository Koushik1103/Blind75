#O(nk)
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        sorted_nums = set(nums)
        count = 0
        for i in nums:
            if i-1 not in sorted_nums:
                length=1
                while i+length in sorted_nums:
                    length+=1
                
                count = max(length, count)
        return count
