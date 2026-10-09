       
""" ================================== LeetCode Version ======================================

- Time Complexity: O(n) 
- Space Complexity: O(1) 

 class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        min_price = prices[0]
        max_profit = 0

        for price in prices[1:]:  #Skip the first element since we already initialized it to min_price.
            if price < min_price:
                min_price = price
                
            elif price - min_price > max_profit:
                max_profit = price - min_price
        
        return max_profit    
========================================================================================== """

# ================================== Runnable Version ======================================

class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        min_price = prices[0]
        max_profit = 0

        for price in prices[1:]:  #Skip the first element since we already initialized it to min_price.
            if price < min_price:
                min_price = price
                
            elif price - min_price > max_profit:
                max_profit = price - min_price
        
        return max_profit

sol = Solution()
n = int(input("Enter the number of days : "))   

prices = list(map(int, input("Enter the prices for each day separated by space : ").split()))
result = sol.maxProfit(prices)
print("Maximium profit is :", result)