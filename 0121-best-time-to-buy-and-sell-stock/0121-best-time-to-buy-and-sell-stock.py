class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        rez = 0
        minim = prices[0]
        for price in prices: 
            if minim > price:
                minim = price
            rez = max(rez, price - minim)

        return rez