#funtion for checkin if input data is correct
def is_only_brackets(sentence):
    for char in sentence:
        if char != '(' and char != ')':
            return False
    return True

def is_input_correct(sentence):
    index = 0
    opening_brackets_list = []
    closing_brackets_list = []

    while index < len(sentence):
        if sentence[index] == '(':
            opening_brackets_list.append(index)
            closed_index = sentence.find(')', index)  # Start searching from the current index
            while closed_index in closing_brackets_list:
                closed_index = sentence.find(')', closed_index + 1)  # Search from the next index
                if closed_index == -1:
                    return False
            closing_brackets_list.append(closed_index)

        elif sentence[index] == ')':
            if index not in closing_brackets_list:
                return False

        index += 1

    return True

while True:
    sentence = str(input("Enter brackets or enter to quit: "))
    while not is_only_brackets(sentence):
        sentence = str(input("Enter brackets or enter to quit: "))
    if sentence == '':
        break
    elif is_input_correct(sentence):
        print("sentence is correct")

    else:
        print("sentence is incorrect")
    #checking input data
