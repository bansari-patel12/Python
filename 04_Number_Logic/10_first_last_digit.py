number = int(input("Enter a number: "))

last_digit = number % 10

first_digit = number

while first_digit >= 10:
    first_digit = first_digit // 10

print("First digit is:", first_digit)
print("Last digit is:", last_digit)