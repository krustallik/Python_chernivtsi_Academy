
def looking_for_word(str1,str2):
    for char in str1:
        if str2.find(char)==-1:
            return False
    return True
while True:
    while True:
        str1 = input("Enter a word or Enter to end: ")
        if str1.isalpha() or str1 == '':
            break
    if str1 == '':
        break
    while True:
        str2 = input("Enter a random letters: ")
        if str1.isalpha():
            break
    if looking_for_word(str1,str2):
        print("Yes")
    else:
        print("No")

