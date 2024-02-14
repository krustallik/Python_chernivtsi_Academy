

distances = {"Тернопіль":"168км","Київ":"485км","Чернігів":"607км",
             "Черкаси":"542км","Вінниця":"256км","Житомир":"349км",
             "Львів":"248км","Івано-Франківськ":"126км","Дніпро":"763км",
             "Одесса":"500км","Миколаїв":"562км","Суми":"810км"}

def looking_for_distance(word):
    if word in distances.keys():
        print("Відстань від чернівців до Вашого міста:",distances[word])
    else:
        print ("відстань до цього міста відсутня в книзі")


while True:
    try:
        word = str(input("Введіть назву міста або Enter щоб закінчити: "))
        if word == '':
            break
        looking_for_distance(word)
    except ValueError:
        print("incorrect input")
