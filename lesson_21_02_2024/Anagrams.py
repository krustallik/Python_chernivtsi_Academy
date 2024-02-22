def are_anagrams(text1, text2):

    text1 = text1.lower().replace(" ", "")
    text2 = text2.lower().replace(" ", "")

    if len(text1) != len(text2):
        return False

    list1 = list(text1)
    list2 = list(text2)

    list1.sort()
    list2.sort()

    if list1 == list2:
        return True
    else:
        return False


text1 = input("Enter first text: ")
text2 = input("Enter second text: ")


if are_anagrams(text1, text2):
    print("this text is anagram.")
else:
    print("This text isn't anagram.")
