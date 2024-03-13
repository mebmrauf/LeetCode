# 29. Divide Two Integers
# https://leetcode.com/problems/divide-two-integers/

class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        # Constants for 32-bit integer range
        INT_MAX = 2**31 - 1
        INT_MIN = -2**31

        # Handle edge cases
        if dividend == 0:
            return 0
        if divisor == 1:
            return min(INT_MAX, max(INT_MIN, dividend))
        if divisor == -1:
            return min(INT_MAX, max(INT_MIN, -dividend))

        # Determine sign of the result
        negative = (dividend < 0) != (divisor < 0)

        # Make dividend and divisor positive for simplicity
        dividend = abs(dividend)
        divisor = abs(divisor)

        quotient = 0
        # Subtract divisor from dividend until dividend becomes smaller
        while dividend >= divisor:
            # Find the largest multiple of divisor which is less than or equal to dividend
            multiple = 1
            divisor_tmp = divisor
            while dividend >= divisor_tmp:
                dividend -= divisor_tmp
                quotient += multiple
                multiple <<= 1
                divisor_tmp <<= 1

        # If the result is negative, negate it
        if negative:
            quotient = -quotient

        # Check if result is within 32-bit integer range
        if quotient > INT_MAX:
            return INT_MAX
        elif quotient < INT_MIN:
            return INT_MIN
        else:
            return quotient