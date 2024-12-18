# 1475. Final Prices With a Special Discount in a Shop
# https://leetcode.com/problems/final-prices-with-a-special-discount-in-a-shop/

from typing import List

class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        length = len(prices)
        if length == 1:
            return prices
        
        i, j, arr = 0, 1, prices[:]
        
        while i < length:
            if j < length and prices[i] >= prices[j]:
                arr[i] = arr[i] - arr[j]
                i += 1
                j = i + 1
            elif j == length:
                i += 1
                j = i + 1
            else:
                j += 1
        
        return arr