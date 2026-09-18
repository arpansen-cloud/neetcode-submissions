class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        #we know that we want to output the amount of "days" it takes to reach the next greater temperature. So basically we are subracter the greater tempind from the lower temp ind, for this we need to keep track of the temperatures and its indices
        #to keep track of previous temperatures and indices we can use a stack and pop the values when we find the next greater temperature 

        days = [0] * len(temperatures)

        stack = []

        for tempind, temp in enumerate(temperatures):

            while stack and temp > stack[-1][0]:

                stackTemp, stackInd = stack.pop()

                days[stackInd] = (tempind - stackInd)

            stack.append([temp,tempind])

        return days 
