
def create_field():
    field = []
    for i in range(1,4):
        field.append([])
        for j in range(i*3-2,i*3+3-2):
            field[i-1].append(j)
    return field

def print_field(field):
    for i in range(3):
        print()
        print("-"*13)
        for j in range(3):
            print("| {} ".format(field[i][j]),end='')

        print("|",end = '')
    print()
    print("-" * 13)


def player_move(field):
    move = -1
    while True:
        try:
            move = int(input("Ваш хід (1-9): ")) - 1
            row, col = move // 3, move % 3
            if field[row][col] not in ["X", "O"]:
                field[row][col] = "O"
                break
            else:
                print("Це поле вже зайняте, спробуйте інше.")
        except ValueError:
            print("Будь ласка, введіть число від 1 до 9.")
        except IndexError:
            print("Введіть число від 1 до 9.")

playing_field = create_field()
print_field(playing_field)
player_move(playing_field)
print_field(playing_field)