
alphabet = "'абвгґдеєжзиіїйклмнопртстуфхцчшщьюя'"

def encrypt(word):
    word = word.lower()
    word = list(word)
    for i in range(len(word)):  # Вам потрібно використовувати range() замість len() для ітерації по довжині списку
        index = alphabet.find(word[i])
        if index == len(alphabet) - 1:
            word[i] = alphabet[0]
        elif index == len(alphabet) - 2:
            word[i] = alphabet[1]
        elif index == len(alphabet) - 3:
            word[i] = alphabet[2]
        elif index != -1:  # Доданий перевірка, щоб уникнути виходу за межі списку при відсутності символу у алфавіті
            word[i] = alphabet[index + 3]
    return ''.join(word)  # Перетворюємо список назад у рядок за допомогою ''.join()

def decrypt(word):
    word = word.lower()
    word = list(word)
    for i in range(len(word)):
        index = alphabet.find(word[i])
        if index == 0:
            word[i] = alphabet[-1]
        elif index == 1:
            word[i] = alphabet[-2]
        elif index == 2:
            word[i] = alphabet[-3]
        elif index != -1:
            word[i] = alphabet[index - 3]
    return ''.join(word)

