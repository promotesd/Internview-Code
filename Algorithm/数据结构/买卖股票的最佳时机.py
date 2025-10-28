from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        ans=0
        minPrice=prices[0]
        for price in prices:
            ans=max(ans, price-minPrice)
            minPrice=min(minPrice, price)
        return ans