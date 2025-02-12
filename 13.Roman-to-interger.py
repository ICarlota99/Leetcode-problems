def main():
    print(Solution().romanToInt("MCMXCIV"))

class Solution:
    def romanToInt(self, s: str) -> int:
        romanNumbers={
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }

        result = 0
        n = romanNumbers["M"]
        for char in s:
            num = romanNumbers[char]
            if n >= num:
                n = num
                result += num
            else:
                result = result + (num - 2 * n) 
                n = num

        return result


main()