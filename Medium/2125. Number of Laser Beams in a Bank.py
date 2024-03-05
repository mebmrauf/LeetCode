# 2125. Number of Laser Beams in a Bank
# https://leetcode.com/problems/number-of-laser-beams-in-a-bank/description/

class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        # Variable to store the count of devices (1s) in the last non-empty row
        lCount = 0

        # Variable to store the total number of beams formed
        tBeams = 0

        # Iterate over each row in the bank
        for row in bank:
            # Count the number of devices ('1's) in the current row
            cCount = row.count('1')

            # If the current row is not empty, proceed with calculations
            if cCount > 0:
                # Add the number of beams formed between the last non-empty row and the current row
                tBeams += lCount * cCount

                # Update the lCount to be the current row's count for the next iteration
                lCount = cCount

        # Return the total number of beams formed
        return tBeams