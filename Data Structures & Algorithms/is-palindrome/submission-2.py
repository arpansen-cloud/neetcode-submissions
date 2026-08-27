class Solution:
    def isPalindrome(self, s: str) -> bool:

        OnlyLetters = []

        for i in s:

            if i.isalnum():
                OnlyLetters.append(i.lower())
        
        if len(OnlyLetters) <= 1 : return True
        
        left, right = 0, len(OnlyLetters) - 1

        while left < right:

            if OnlyLetters[left] != OnlyLetters[right]: return False
        
            left += 1
            right -= 1

        return True



        