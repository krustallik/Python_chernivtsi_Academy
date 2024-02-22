
#funktion for enterring data
def enter_data():
    while True:
        try:
            text = input("Enter data: ")
            text = text.replace(" ", "")
            if len(text) == 81 and text.isdigit():
                return text
                break
            else:
                print("Incorrect value")
        except ValueError:
            print("Incorrect Value")

# funktion to print matrix better
def print_matrix(matrix,row,column):
    for i in range(row):
        print(matrix[i])



#funktion for making matrix to better look
def making_matrix_from_line(line):
    index = 0
    data_in_matrix = []
    for i in range(9):
        data_in_matrix.append([])
        for j in range(9):
               data_in_matrix[i].insert(j,data_in_line[index])
               index += 1

    return data_in_matrix


def is_right(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):

            # checking rows
            for row_ind in range(len(matrix)):
                if row_ind != j and matrix[i][row_ind] == matrix[i][j]:
                    return False

            # checking columns
            for col_ind in range(len(matrix[0])):
                if col_ind != i and matrix[col_ind][j] == matrix[i][j]:
                    return False

            # Checking squares
            for ind1 in range(0, len(matrix), 3):
                for ind2 in range(0, len(matrix[0]), 3):
                    square_values = []

                    for i in range(ind1, ind1 + 3):
                        for j in range(ind2, ind2 + 3):
                            value = matrix[i][j]

                            # Check if the value is already in the square
                            if value in square_values:
                                return False
                            else:
                                square_values.append(value)

    return True



data_in_line = enter_data()
data_in_line = list(data_in_line)

data_in_matrix = making_matrix_from_line(data_in_line)
print_matrix(data_in_matrix,len(data_in_matrix),len(data_in_matrix[0]))

if is_right(data_in_matrix):
    print("Input for sudoku is correct")
else:
    print("Input for sudoku isn't correct")
