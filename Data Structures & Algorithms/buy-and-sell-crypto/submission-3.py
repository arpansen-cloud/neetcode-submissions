class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
       #if I was solving this without code, I would choose the max value to the right of my current value that I am looking at. And then calcualte the difference between those two for the profit. This would give me the maxProfit 

       #for coding I can take the sliding window approach and start from one pointer on the left and use my right pointer to increment through the values, if my starting (left) pointer is > my right pointer I can have to increase the index of the left pointer by having it equal to the right pointerm. and becasue we want to increase the window we can add one to the right value to go increase our indexing in the array.  

        #for my loop, I can use the condition of while the moving pointer is < len(arr). for the math I can iniate a max_profit var to increase the amount of max profit over the loop. the profit would be equal to the number on the right pointer - starting number


        left, right = 0, 1

        max_profit = 0 

        while right < len(prices):
            if prices[left] < prices[right]:
                profit = prices[right] - prices[left]

                max_profit = max(max_profit, profit)

            else:
               left = right
            right +=1 

        return max_profit
        