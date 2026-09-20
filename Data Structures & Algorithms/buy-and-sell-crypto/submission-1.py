class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        #[3,2,7,3,1], basically look for a delta that is positive
        maxp=float('-inf')
        for i in range(len(prices)):
            if i+1<len(prices):
                for j in range(i+1,len(prices)):
                    if prices[j]-prices[i] > 0 and prices[j]-prices[i]>maxp:
                        profit = prices[j]-prices[i]
                        maxp= profit
        return max(0,maxp)