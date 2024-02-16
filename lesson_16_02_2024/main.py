# main.py
from caesar_cipher import encrypt, decrypt

while True:
    try:
        temp = int(input("Enter 1 to encrypt, 2 to decrypt, or any other number to quit: "))
    except ValueError:
        print("invalid input")
    if temp == 1:
        word_to_encrypt = str(input("Enter a word to encrypt by Caesar encryptor: "))
        while not word_to_encrypt.isalpha():
            word_to_encrypt = str(input("Enter a word to encrypt by Caesar encryptor: "))

        encrypted_word = encrypt(word_to_encrypt)
        print("Encrypted word is:", encrypted_word)
    elif temp == 2:
        word_to_decrypt = str(input("Enter a word to decrypt by Caesar encryptor: "))
        while not word_to_decrypt.isalpha():
            word_to_decrypt = str(input("Enter a word to decrypt by Caesar encryptor: "))

        decrypted_word = decrypt(word_to_decrypt)
        print("Decrypted word is:", decrypted_word)
    else:
        break
