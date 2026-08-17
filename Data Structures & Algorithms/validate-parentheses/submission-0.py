class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        closetoOpen = {
            ")" : "(",

            "]" : "[",

            "}" : "{"
        }

        for i in s:

            if i in closetoOpen:
                if stack and stack[-1] == closetoOpen[i]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(i)
        
        return True if not stack else False 