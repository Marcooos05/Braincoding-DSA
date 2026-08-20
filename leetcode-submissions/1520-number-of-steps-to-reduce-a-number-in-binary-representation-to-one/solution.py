class Solution:
    def numSteps(self, s: str) -> int:
        total = 0
        carry = 0
        for i in range(len(s)-1,-1,-1):
            if i == 0 and carry == 0:
                return total
            elif i == 0 and carry == 1:
                return total + 1

            if s[i] == '1' and carry == 0:
                total += 2
                carry = 1
            elif s[i] == '1' and carry == 1:
                total += 1
                carry = 1
            elif s[i] == '0' and carry == 0:
                total += 1
            elif s[i] == '0' and carry == 1:
                total += 2
                carry = 1
