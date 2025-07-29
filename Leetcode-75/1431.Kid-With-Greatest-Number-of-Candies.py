class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        output = []
        max_candies = 0

        for kids_candies in candies:
            if kids_candies > max_candies:
                max_candies = kids_candies

        for kids_candies in candies:
            if kids_candies + extraCandies >= max_candies:
                output.append(True)
            else:
                output.append(False)
        return output

# Runtime 0ms O(N)
# Memory 17.67MB O(1)