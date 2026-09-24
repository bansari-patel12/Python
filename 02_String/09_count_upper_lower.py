str = input("Enter string: ")

print("The string is: ",str)

low = 0
up = 0

# if str in str.lower():
#     low += 1

# else:
#     up += 1
    

for i in str:
    if i.islower():
        low += 1

    else:
        up += 1
        
print("Total lower latter in string is: ",low)
print("Total upper latter in string is: ",up)