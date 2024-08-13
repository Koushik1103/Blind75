#stack O(n), Space O(n) cause stack can take space == size of input str
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        d = {'}':'{', ']':'[', ')':'('} #mapping close to open cause top should always close

        for char in s:
            if char in d:
                #check if stack is there and top of stack is equal to a key in dict
                if stack and stack[-1]==d[char]:
                    #if so remove the top element
                    stack.pop()
                else:
                    return False #cause doesnt match, final top element should close
            else:
                #push to stack if open bracket
                stack.append(char)

        return True if not stack else False #if stack empty T else F
