def main():
    # Prompt user for input
    n = get_n()
    k = get_k(n)

    # Number of total possible combinations
    c = total_combinations(n, k)
    array = []

    my_set = set()
    for i in range(c):
        for j in range(n):
            my_set.add(new_value(k, j))

            if len(my_set) == k:
                if my_set not in array:
                    array.insert(i, my_set)
                    my_set.clear()

    print(f"{array}")
            

# Check for input correctness
def get_n():
    n = 0
    while not(1 <= n <= 20):
        try:
            print("Please, insert a number between 1 - 20.")
            n = int(input("n = "))
        except ValueError:
            print("Not an interger")   
    return n

def get_k(n):
    k = 0 
    while not(1<= k <= n):
        try:
            print(f"Please, insert a number between 1 - {n}.")
            k = int(input("k = "))
        except ValueError:
            print("Not an interger")
    return k


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
    

main()