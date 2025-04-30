class Solution:
    def getSum(self, a: int, b: int) -> int:
        MAX = 0xFFFFFFFF
        MASK = 0x7FFFFFFF

        while b != 0:
            carry = a & b         # calculate carry
            a = (a ^ b) & MAX     # calculate sum without carry, limit to 32 bits
            b = (carry << 1) & MAX  # shift carry left and limit to 32 bits

        # if a is negative in 32-bit, convert to Python’s negative
        return a if a <= MASK else ~(a ^ MAX)
