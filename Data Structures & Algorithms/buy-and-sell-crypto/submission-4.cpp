class Solution {
public:
    int maxProfit(vector<int>& prices) {
        if (prices.size() == 0) {
            return 0;
        }
        
        int lowestPrice = prices[0];
        int bestProfit = 0;

        for (int i = 1; i < prices.size(); i++) {
            bestProfit = max(bestProfit, prices[i] - lowestPrice);
            if (lowestPrice > prices[i]) {
                lowestPrice = prices[i];
            }
        }
        return bestProfit;
    }
};
