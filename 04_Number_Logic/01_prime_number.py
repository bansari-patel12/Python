number = int(input("Enter a number: "))

count = 0
i = 1

while i <= number:
    if number % i == 0:
        count = count + 1

    i = i + 1

if count == 2:
    print("The number is Prime")
else:
    print("The number is not Prime")