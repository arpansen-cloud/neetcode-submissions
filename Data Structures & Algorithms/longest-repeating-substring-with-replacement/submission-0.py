class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        #solve this without code, solve it like a human, check for the instances where there is an amount of "K" characters that appear that are inbetween distinct characters. Through this I can find the max length of the window that is valid to replace within the string.

        #with code I would setup a dictionary that holds the characters to the amount of time they appear, I would initiate a result var and a var that holds the max occurences of characters. through this I would increase the window side by subtracting r index from left and + 1 to it because python indexes at 0. In the occurance that the window size exceeds the k amount while hitting the end of the right pointers I would subtract the occurance from the left pointer index and I would increase the position of the left pointer to decrease the window size. 

        char_occurance= {}

        result =0

        max_freq = 0
        left = 0

        for r in range(len(s)):

            char_occurance[s[r]] = 1 + char_occurance.get(s[r],0)

            max_freq = max(max_freq, char_occurance[s[r]])

            while (r - left + 1 ) - max_freq > k:
                char_occurance[s[left]] -= 1 

                left += 1

            result = max(result, r -left + 1)
        return result