class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        #intiate a result variable, sort the numbers so you can hold on to first value and then split the problem into tow sum II to get numbers that equal to 0 

        #setup a loop that holds onto first value ensures that value will not be repeated. setup left and right pointers, the greater numbers will be on the right side while the smaller numbers will be on the left side. 
        #check if total == 0, if so return the left and right number and also the first value, check if the total < 0, increase left pointer, check if total is > 0, increase right pointer. 
        #because it is sorted we want to make sure that the outputted left and right vals are not repeated so you want to setup a loop that checks for repeat value, if repeated only update one pointer. (only need to update one pointer because it is sorted)

        res = []

        nums = sorted(nums)
        
        for i, val in enumerate(nums):

            if i > 0 and val == nums[i-1]:
                continue
            
            left, right = i+1 , len(nums) -1 

            while left < right:

                total = val + nums[left] + nums[right]

                if total < 0:
                    left += 1
                
                elif total > 0:
                    right -= 1

                else:
                    res.append([val, nums[left],nums[right]])

                    left+=1
                    while nums[left] == nums[left -1] and left < right:

                        left += 1

        return res



