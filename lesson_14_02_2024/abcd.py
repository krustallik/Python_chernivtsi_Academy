

dictionary = {"собака":"Dog","кіт":"Cat","мама":"Mother","дерево":"Tree","камінь":"Stone","трава":"Grass",}

def looking_for_word(word):
    if word in dictionary.keys():
        print("translate of your word is:",dictionary[word])
    else:
        print ("this is invalid word")

while True:
    try:
        word = str(input("Enter any word in ukrainian language to translate or Enter to end: "))
        if word == '':
            break
        looking_for_word(word)
    except ValueError:
        print("incorrect input")

