number = 2

while number <= 100:
    count = 0
    i = 1

    while i <= number:
        if number % i == 0:
            count = count + 1

        i = i + 1

    if count == 2:
        print(number)

    number = number + 1