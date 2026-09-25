number = int(input("Enter a number: "))

original = number
sum = 0

while number != 0:
    digit = number % 10
    sum = sum + digit ** 3
    number = number // 10

if sum == original:
    print("The number is an Armstrong Number")
else:
    print("The number is not an Armstrong Number")