str = input("Enter a string: ")

vowels = 0

for i in str:
    if i in "aeiouAEIOU":
        vowels += 1

    else:
        pass
print("The string is: ",str)
print("Total vowels precent in string is: ",vowels)
