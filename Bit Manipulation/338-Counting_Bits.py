#dp problem watch neetcode for explanation of offset
class Solution:
    def countBits(self, n: int) -> List[int]:
        dp = [0]*(n+1)
        offset = 1

        for i in range(1, n+1):
            if offset*2 == i:
                offset = i
            dp[i] = 1 + dp[i - offset]
        return dp
        
'''
0000-0
0001-1
0010-1
0011-2
0100-1
0101-2
0110-2
0111-3
1000-1
last two bits repeat after every 4 numbers
3rd bit from last is offset, where 1 exist in the next 4 nums
so dp[i]=1+dp[i-offset], i=4 means 4-4=0 so dp[0]=0, dp[4] would be 1
'''
