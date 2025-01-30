from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Define an output list
        numbers = []
        # Order the input list in descending order
        ordered_nums = []
        ordered_nums.extend(nums)
        ordered_nums.sort(reverse=True)
            
        # Search for combinations in the input list
        for number in ordered_nums:
            second_number = target - number
            if second_number == number:
                indexes = [i for i, num in enumerate(nums) if num == number]
                if len(indexes)==2:
                    return(indexes)
            elif second_number in ordered_nums:
                numbers.append(nums.index(number))
                numbers.append(nums.index(second_number))
                return(numbers)

# Time and Space complexity: O(n)
# Choose this solution because search is faster