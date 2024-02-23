import random
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
    print('Гравець ходить: ')
    move = -1
    while True:
        try:
            #Перевірка коректності ходу гравця
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
    print_field(field)
def computer_move(field):
    print('Комп\'ютер ходить: ')
    free_cells = []
    for row in range(3):
        for col in range(3):
            if field[row][col] not in ["X", "O"]:
                free_cells.append((row, col))

    if free_cells:
        # Перевіряємо можливість перемоги гравця або блокування гравця
        for row, col in free_cells:
            test_field = [row[:] for row in field]

            # Спробуємо розмістити символ комп'ютера у цій клітинці і перевіримо, чи виграє гравець
            test_field[row][col] = "X"
            if is_end(test_field) == "X":
                field[row][col] = "X"
                print_field(field)
                return
            else:
                # Спробуємо розмістити символ гравця у цій клітинці і перевіримо, чи виграє гравець
                test_field[row][col] = "O"
                if is_end(test_field) == "O":
                    field[row][col] = "X"
                    print_field(field)
                    return

        # Якщо немає можливості перемогти або блокувати, просто робимо випадковий хід
        row, col = random.choice(free_cells)
        field[row][col] = "X"
    else:
        print("Немає вільних клітинок.")
    print_field(field)




def is_end(field):
    # Перевірка рядків і стовпців
    for i in range(3):
        if field[i][0] == field[i][1] == field[i][2]:  # Перевірка рядків
            return field[i][0]
        if field[0][i] == field[1][i] == field[2][i]:  # Перевірка стовпців
            return field[0][i]

    # Перевірка діагоналей
    if field[0][0] == field[1][1] == field[2][2] or field[0][2] == field[1][1] == field[2][0]:
        return field[1][1]

    # Перевірка на нічию
    elif turn_ind == 9:
        return 'Draw'
    return False  # Гра продовжується

turn_ind = 0

def game_loop(field):
    global turn_ind
    turn = random.choice(['player', 'computer'])  # Вибір, хто ходить першим
    print(f"{turn} починає гру!")

    while True:
        if turn == 'player':
            player_move(field)
            turn_ind += 1
            if is_end(field) != False:
                break
            turn = 'computer'
        else:
            computer_move(field)
            turn_ind += 1
            if is_end(field) != False:
                break
            turn = 'player'


if __name__ == "__main__":

    playing_field = create_field()
    print_field(playing_field)
    game_loop(playing_field)

    if is_end(playing_field) == 'Draw':
        print('Нічия')
    elif is_end(playing_field) == 'X':
        print('Виграв компютер')
    elif is_end(playing_field) == 'O':
        print('Виграв гравець')
