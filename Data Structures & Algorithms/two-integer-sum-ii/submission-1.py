class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        #array is already sorted need to add up to target, cannot be the same index
        #use two pointers to get total value of both left and right number
        #compare total value to target, if it is equal to the target you can return the index of left +1 and right + 1 because we want the 1-indexed indicie
        #else we can increase the left pointer and the right pointer and
        #if total is < target increase the left pointer because the lower values are always going to be on the left side
        #if the total is greater than target decrease the right pointer because greater values is on the right side

        left, right = 0, len(numbers) -1 

        while left < right:

          total = numbers[left] + numbers[right]

          if total == target:
               return [left + 1, right + 1]

          elif total < target:
               left +=1 
               
          else:
               right -= 1 
     

          