"""
    Given an integer num, return the number of steps to reduce it to zero.
    In one step, if the current number is even, you have to divide it by 2, otherwise, you have to subtract 1 from it.
"""
# Easy # Math #Bit Manipulation # Recursive
def steps(n):
    if n == 0:
        return 0
    elif n % 2 == 0:
        return steps(n/2) + 1
    else:
        return steps(n-1) + 1

class Solution:
    def numberOfSteps(self, num: int) -> int:
        return steps(num)
    
# Solution 2 Optimized Bitwise Operation 
# (NOT MINE, from: https://leetcode.com/problems/number-of-steps-to-reduce-a-number-to-zero/solutions/6397373/two-solutions-looping-integer-operations-bitwise-operation/)
class Solution:
    def numberOfSteps(self, num: int) -> int:

        if num == 0:
            return 0
        return num.bit_length() + bin(num).count('1') - 1