def is_palindrome(self, x):
    if x < 0 :
        return False

    rev = 0
    num = x

    while num != 0:
        rev = rev * 10 + num % 10
        num //= 10
    return rev == x

x = int(input("Enter a number: "))

print(is_palindrome(None, x))