def main():
    number = int(input("Insert a number: "))
    print(isPalindrome(number))


def isPalindrome(x):
    reverse = 0
    buffer = x
    while buffer > 0:
        remainder = buffer % 10
        reverse = reverse * 10 + remainder
        buffer = buffer // 10
    return reverse == x
    

main()