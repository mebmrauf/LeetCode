# 1352. Product of the Last K Numbers
# https://leetcode.com/problems/product-of-the-last-k-numbers/

class ProductOfNumbers:
    def __init__(self):
        self.nums = []
        self.products = [1]

    def add(self, num: int) -> None:
        if num == 0:
            self.nums = []
            self.products = [1]
        else:
            self.nums.append(num)
            self.products.append(self.products[-1] * num)

    def getProduct(self, k: int) -> int:
        if k > len(self.nums):
            return 0
        return self.products[-1] // self.products[-k-1]
        
# Time complexity: O(1) for add and getProduct

# Your ProductOfNumbers object will be instantiated and called as such:
# obj = ProductOfNumbers()
# obj.add(num)
# param_2 = obj.getProduct(k)