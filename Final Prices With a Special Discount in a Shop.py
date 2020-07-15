class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        i = 0
        l = len(prices)
        while i < l - 1:
            j = i + 1
            while j < l and prices[j] > prices[i]:
                j += 1
            if j < l and prices[i] >= prices[j]:
                prices[i] = prices[i] - prices[j]
            i += 1
        return prices