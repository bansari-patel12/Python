number = int(input("Enter a number: "))


print("The  Number is: ",number)

sum = 0
digit = number % 10

if digit % 10 == 0:
    sum = sum + digit
    number // 10

else:
    pass





print("Total Even digits are: ",digit)
