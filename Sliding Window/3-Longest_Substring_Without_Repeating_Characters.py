#sliding window O(n)
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        charSet = set()
        l = 0
        result = 0

        for i in range(len(s)):
            while s[i] in charSet:
                charSet.remove(s[l]) #remove s[l] cause first repeating char then second ...
                l += 1
            charSet.add(s[i])
            result = max(result, i-l+1)
        
        return result
