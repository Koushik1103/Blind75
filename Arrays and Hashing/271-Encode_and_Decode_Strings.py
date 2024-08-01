class Solution:
    def encode(self, strs: List[str]) -> str:
        res_str = ""
        for i in strs:
            res_str += str(len(i)) + "#" + i
        return res_str
    
    def decode(self, s: str) -> List[str]:
        res_list = []
        i = 0
        while i<len(s):
            j=i
            while s[j] != "#":
                j+=1
            length = int(s[i:j])
            i = j+1
            j = i+length
            res_list.append(s[i:j])
            i=j
        return res_list
