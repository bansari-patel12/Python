num = int(input("Enter a number: "))

sum = 0
digit = 0

while num != 0:
    digit = num % 10
    num = num // 10
    sum = sum + digit

print(f"Sum of numbers is: {sum}")
