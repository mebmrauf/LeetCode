# 1291. Sequential Digits
# https://leetcode.com/problems/sequential-digits/description/

class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        result = []
        
        for digit in range(1, 10):
            num = digit
            nextDigit = digit + 1
            
            while nextDigit <= 9:
                num = num * 10 + nextDigit
                if low <= num <= high:
                    result.append(num)
                elif num > high: break
                nextDigit += 1
        
        return sorted(result)