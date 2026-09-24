str = input("Enter a string: ")

const = 0

for i in str:
    if i not in "aeiouAEIOU":
        const += 1

    else:
        pass

print("The string is : ",str)
print("Total Consonants  is: ",const)