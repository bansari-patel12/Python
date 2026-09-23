number = int(input("Enter a number:"))

if number % 5 == 0 and number % 10 == 0:
    print(f"{number} is a divisible by 5 and 10")

else:
    print(f"{number} is not divisible by 5 and 10")