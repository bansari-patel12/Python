str = input("Enter a string: ")

print("The String is: ",str)

if str == str[::-1]:
    print("The string is a palindrome")

else:
    print("The string is not a palindrome")