
def palindrome_checker(sentence):
    sentence = sentence.lower()
    sentence = list(sentence)
    try:
        for i in range(len(sentence)):
            if sentence[i] == ' ':
                del(sentence[i])
    except IndexError:
        pass
    if sentence == sentence[::-1]:
        return True
    else:
        return False

while True:
    sentence = str(input("Enter a sentence to check if it is palindrome: "))
    if palindrome_checker(sentence):
        print("It's palindrome")
    else:
        print("It's not palindrome")
    break