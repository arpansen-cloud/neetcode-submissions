class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
       
        left, right = 0, len(nums) - 1

        middle = (left + right) // 2
        while left <= right:

            if target == nums[middle]: return middle

            elif target == nums[left] : return left

            elif target == nums[right] : return right

            else : 

                left += 1 

                right -= 1
        return -1
