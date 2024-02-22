def checking(min, max):
    while True:
        try:
            number = int(input("Enter number in diapason {} -> {}: ".format(min, max)))
            if -min <= number <= max:
                print("correct number")
                break

        except ValueError:
            print("incorrect value")


up_diapasnon = 10
bottom_diapason = -10
checking(bottom_diapason,up_diapasnon)
