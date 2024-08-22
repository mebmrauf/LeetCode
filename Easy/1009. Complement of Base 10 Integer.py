# 1009. Complement of Base 10 Integer
# https://leetcode.com/problems/complement-of-base-10-integer/

class Solution:
    def bitwiseComplement(self, n: int) -> int:
        if n == 0:
            return 1
        # convert decimal to binary
        binaryNumber = ''
        while n > 0:
            binaryNumber = str(n%2) + binaryNumber
            n = n//2

        # reverse the binary number
        reverseBinaryNumber = ''
        for i in binaryNumber:
            if i == '1':
                reverseBinaryNumber += '0'
            else:
                reverseBinaryNumber += '1'

        #convert binary to deciaml
        reverseNumber = 0
        l = len(reverseBinaryNumber) - 1
        for i in reverseBinaryNumber:
            reverseNumber += 2**l * int(i)
            l -= 1
        return reverseNumber