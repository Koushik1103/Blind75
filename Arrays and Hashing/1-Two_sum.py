#Hashmap O(n)
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = {}
        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in d:
                return d[complement],i
            d[nums[i]] = i
        return []
        
#Two for loops O(n^2)
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        final = []
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i]+nums[j] == target:
                    final.append(i)
                    final.append(j)
        return final        
