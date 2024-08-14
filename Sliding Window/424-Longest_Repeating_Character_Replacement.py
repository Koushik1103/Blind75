#O(26*n) = O(n) because 26 caps alphabets
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        d = {} #count for char in s
        count = 0 #max substring len will be updated
        lp = 0

        for rp in range(len(s)):
            d[s[rp]] = 1+d.get(s[rp], 0)
            #window size - max value > k to see how many to be replaced
            #if not lp+=1
            while (rp-lp+1)-max(d.values())>k:
                d[s[lp]] -= 1 #left pointer char freq -1
                #cause window size reduce
                lp += 1
            count = max(count, rp-lp+1)
        return count
