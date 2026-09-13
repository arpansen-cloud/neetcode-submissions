class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
    #loop through the nums, multiply everything by the left side and right side. 
    #have a way to hold the result and way to hold what you are multiplying the numbers by. throughout the loop you can update those variables from left to right. 
    #[1,2,3,4,6] 

        result = [1] * len(nums)

        prefix = 1 

        for i in range(len(nums)):
            result[i] = prefix #nothing to the left of 1, so just 1 
            prefix *= nums[i]

        postfix = 1
            
        for i in range(len(nums) - 1, -1, - 1):

            result[i] *= postfix

            postfix *= nums[i]

        return result 