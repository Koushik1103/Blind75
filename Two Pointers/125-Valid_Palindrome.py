#usual O(n)
class Solution:
    def isPalindrome(self, s: str) -> bool:
        new_s = ("".join(i for i in s if i.isalnum())).lower()
        return new_s==new_s[::-1]
        
#Two Pointers
class Solution:
    def isPalindrome(self, s: str) -> bool:
        lp = 0
        rp = len(s)-1
        while(lp<rp):
            while lp<rp and not s[lp].isalnum(): lp+=1
            while lp<rp and not s[rp].isalnum(): rp-=1

            if s[lp].lower() != s[rp].lower(): return False
            lp+=1
            rp-=1
        return True
