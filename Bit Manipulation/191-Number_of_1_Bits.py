#Method 1 - O(32) or O(n)
class Solution:
    def hammingWeight(self, n: int) -> int:
        count = 0
        while n: #while num is > 0
            count += n%2 #if last digit is 1, %2 will return 1
            n = n >> 1 #right shift 0101->010
        return count
        
        
#Method 2 - O(32) or O(n)
class Solution:
    def hammingWeight(self, n: int) -> int:
        count = 0
        while n: #while num is > 0
            n = n & n-1 #watch the neetcode video
            count += 1
        return count
