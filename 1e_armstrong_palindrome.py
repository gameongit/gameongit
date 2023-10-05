def is_armstrong(num):
    sum = 0
    temp = num
    while temp > 0:
        digit = temp % 10
        sum += digit ** 3
        temp //= 10
    return num == sum

def is_palindrome(num):
    return str(num) == str(num)[::-1]

num = int(input("Enter a number to check if it is an Armstrong or not: "))
if is_armstrong(num):
    print(num, "is an Armstrong number")
else:
    print(num, "is not an Armstrong number")

num = int(input("Enter a number to check if it is a palindrome or not: "))
if is_palindrome(num):
    print(num, "is a palindrome number")
else:
    print(num, "is not a palindrome")
