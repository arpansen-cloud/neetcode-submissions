class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        #have a list that I can append the alphanumeric values to from the orignal array(append lowercase so everything is the same type of char). I can check for the edge case of the input arr being <= length 1. Check for both the left side and the right side of the new array of alpha num values. (Setup 2 pointers)

        correct_char = []
        for i in s:

            if i.isalnum():
                correct_char.append(i.lower())


        if len(correct_char) <= 1:
            return True

         
        left, right = 0 , len(correct_char) - 1


        while left < right:

            if correct_char[left] != correct_char[right]:
                return False
        
            left+= 1
            right -= 1

        return True
