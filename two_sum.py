def main():
    nums = [2,7,11,15] 
    target = 9
    twoSum(nums, target)


def twoSum(nums, target):
    # Define an output list
    numbers = []
    # Order the input list in descending order
    ordered_nums = []
    ordered_nums.extend(nums)
    ordered_nums.sort(reverse=True)

    # Determine number of elements in list
    size = len(nums)
        
    # Search for combinations in the input list
    for i in range(size):
        if ordered_nums[i] <= target:
            second_number = target - ordered_nums[i]
            if second_number in ordered_nums:
                numbers.append(nums.index(ordered_nums[i]))
                numbers.append(nums.index(second_number))
                print(numbers.sort)
                break

main()