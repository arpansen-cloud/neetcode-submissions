class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        #solve this like a human without code: i would look through s2 using the characters and length of s1 if the characters and the length of s1 exist I can return true, else false. 
    #code: I would have a base case of if s1 > s2 I can return false
    #initiate a count of 26 0's for both strings because there are 26 letters in the alphabet. loop through range of len(s1) and add 1 to those indicies. 
    #if there is a permutation in the beginning we can just return true 
    # else we can initiate a sliding window. left = 0 and then go through with a right pointer index with in the range of len(s1) and stopping at the len(s2))
    #add 1 to where the right index is for each of the counts and we can use the left index to remove 1 where the left index is in the count. this allows us to slide based on the len of s1. finally check if the counts are equal, if they are return true else false 
        if len(s1) > len(s2):
            return False

        countS1 = [0] * 26
        countS2 = [0] * 26

        for i in range(len(s1)):
            countS1[ord(s1[i])- ord("a")] +=1 
            countS2[ord(s2[i]) - ord("a")] +=1 

        if countS1 == countS2: 
            return True
        
        left = 0

        for right in range(len(s1), len(s2)):
            countS2[ord(s2[right]) - ord("a")] += 1
            countS2[ord(s2[left]) - ord("a")] -= 1 

            left += 1

            if countS1 == countS2:
                return True
        
        return False
               

    
    
        