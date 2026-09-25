number = int(input("Enter a number: "))

print("The number is:", number)

largest = 0

while number != 0:
    digit = number % 10

    if digit > largest:
        largest = digit

    number = number // 10

print("Largest digit is:", largest)