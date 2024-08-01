#Two Pointers O(n^2)
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        target = 0
        res = []
        nums.sort()

        for i in range(len(nums)):
            if i>0 and nums[i]==nums[i-1]:
                continue
            
            # i fixed pointer
            j=i+1 #lp
            k = len(nums)-1 #rp

            while j<k:
                sums = nums[i]+nums[j]+nums[k]

                if sums == target:
                    res.append([nums[i], nums[j], nums[k]])
                    j+=1
                    k-=1

                    while j<k and nums[j]==nums[j-1]:
                        j+=1
                    while j<k and nums[k]==nums[k+1]:
                        k-=1
                elif sums<target:
                    j+=1
                else:
                    k-=1
        return res
