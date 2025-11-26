from typing import List
from math import inf

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        ans=0
        minPrice=inf
        for price in prices:
            ans=max(ans, price-minPrice)
            minPrice=min(minPrice, price)
        return ans