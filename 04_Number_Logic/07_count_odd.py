number = int(input("Enter a number: "))
print("the number is: ",number)

sum = 0
digit = number % 10

if digit % 2 != 0:
    sum = sum + digit
    number // 10

else:
    pass

print("Total odd digit is: ",digit)