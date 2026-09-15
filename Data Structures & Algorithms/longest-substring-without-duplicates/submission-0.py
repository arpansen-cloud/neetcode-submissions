class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        #for this question if I were to solve it without code, I can look for the first instance of a character and keep adding the the length of the substring until I see a character that I aready have seen. This will give me the longest possible substring. 

        #for coding I can iniate a set and add values to it if it does not exist within the set if it does, we can remove the value and add one to an incrementer, we can use a sliding window approach where we increase the length of the left side every time we find a char that exist in the set. we can use a right pointer to index for the range of the len of the string . we can update a variable that holds the longest length of a substring. We can update the number by using the max function to compare the number of right index - left index + 1 because in the beginning we need to add 1 when the set has its first value

        char_set = set()

        longest = 0

        left = 0

        for r in range(len(s)):

            while s[r] in char_set:
                char_set.remove(s[left])

                left += 1
            char_set.add(s[r])
            
            longest = max(longest, r-left + 1)

        return longest 