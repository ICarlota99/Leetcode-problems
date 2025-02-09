"""
    Given an array nums. We define a running sum of an array as runningSum[i] = sum(nums[0]…nums[i]).

    Return the running sum of nums.
"""
# Easy # Array # Prefix Sum
class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        sum = 0
        output = []
        for number in nums:
            sum += number
            output.append(sum)

        return output