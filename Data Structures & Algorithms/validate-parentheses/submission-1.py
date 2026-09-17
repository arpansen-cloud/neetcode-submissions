class Solution:
    def isValid(self, s: str) -> bool:
        #we see that a paranthesis is valid when the outsides of the paranthesis contain a open to close paranthesis
        #we can create a hashmap for close to open parantesis, and create a stack that pops out the last value from the stack if the value we are first check is inside of the hashmap and equal to the closed paranthesis at the end of the list. 

        closeToOpen = {
            ")" : "(",
             "}" : "{",
             "]" : "[" }
        stack = [] #last in first out
        for char in s:

            if char in closeToOpen:

                if stack and closeToOpen[char] == stack[-1]:

                    stack.pop()
                else:
                    return False
            else:
                stack.append(char)

        return True if not stack else False
                
