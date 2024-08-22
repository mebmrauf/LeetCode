# 476. Number Complement
# https://leetcode.com/problems/number-complement/

class Solution:
    def findComplement(self, num: int) -> int:
        
        # convert decimal to binary
        binaryNumber = ''
        while num > 0:
            binaryNumber = str(num%2) + binaryNumber
            num = num//2

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