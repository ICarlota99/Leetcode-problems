class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        # Number of total possible combinations
        c = total_combinations(n, k)
        list = []

        if n == 1:
            list = [n]
            return list
        elif k == 1:
            list = [[j for j in range (n)] for i in range(c)]
            return list


# Combinatoria de n en k :V (npi en ingles)
def total_combinations(n, k):
    c = factorial(n) / (factorial(k) * factorial(n - k))
    return int(c)


# Calculate factorial of x
def factorial(x):
    if x == 1:
        return x
    else:
        return x * factorial(x - 1)
    
def new_value(x, y):
    if x == 1:
        return y + 1
    else:
        return new_value(x - 1, y)
    