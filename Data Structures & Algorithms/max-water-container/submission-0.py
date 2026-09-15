class Solution:
    def maxArea(self, heights: List[int]) -> int:
        #get the bars through height indices, use the bars to find the max area which can be determined from multiplying the 2 largest bar heights
        #find the width by subtracting the bar indices and finding abs of them 
        # find the min of the the bar height between those two heights and then sqaure it to get the max possible area.
      
        left, right = 0 , len(heights) - 1
        maxArea = 0
        while left < right:

            width = right - left

            height = min(heights[left], heights[right])
            
            area = height * width
            
            maxArea = max(area, maxArea)

            if heights[left] < heights[right]:

                left += 1

            else:
                right -= 1
        return maxArea








