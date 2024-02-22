

while True:
    try:
        number = int(input("Enter number in diapason -10 -> 10: "))
        if -10 <= number <= 10:
            print("correct number")
            break

    except ValueError:
        print("incorrect value")