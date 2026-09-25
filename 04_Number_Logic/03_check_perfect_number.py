number = int(input("Enter a number: "))

sum = 0
i = 1

while i < number:
    if number % i == 0:
        sum = sum + i

    i = i + 1

if sum == number:
    print("The number is a Perfect Number")
else:
    print("The number is not a Perfect Number")