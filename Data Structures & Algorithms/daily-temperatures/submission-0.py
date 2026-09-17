class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        days = [0] * len(temperatures)

        stack = [] #pair of temp, index 

        for tempind, temp in enumerate(temperatures):

            while stack and temp > stack[-1][0]:
                stackT, stackInd = stack.pop()
                days[stackInd] = (tempind - stackInd)
            stack.append([temp, tempind])

        return days