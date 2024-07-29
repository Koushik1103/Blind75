#HashTable O(n)
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        else:
            d1 = {}
            d2 = {}
            for i in s:
                if i in d1.keys():
                    d1[i]+=1
                else:
                    d1[i]=1
            for i in t:
                if i in d2.keys():
                    d2[i]+=1
                else:
                    d2[i]=1   
            return d1==d2   
            
#Sorting O(n log n)
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sorts = sorted(s)
        sortt = sorted(t)
        return sorts==sortt
