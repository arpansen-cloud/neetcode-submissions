class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        #set up two points that check for the specific index from left and right of the array. Use a condition that checks for if the sum of left and right is equal to target. If the condition passes, you can return the indices. 
        #return indices + 1 because we want to return the 1-indexed

        left, right = 0 , len(numbers) -1 


        while left < right:
            
           total = numbers[left] + numbers[right]

           if total == target:
                return [left + 1, right +1]

           elif total < target:
                left += 1 

           else:
             right -= 1
            

        