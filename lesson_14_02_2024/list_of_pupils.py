

list_of_pupils = [
    "Олександр Іваненко","Ірина Петренко","Михайло Ковальчук","Ольга Сидоренко",
    "Андрій Григоренко","Тетяна Мельник","Володимир Павленко","Наталія Коваль",
    "Євген Лисенко","Марія Савченко","Дмитро Кузьменко","Анастасія Онопрієнко",
    "Сергій Бондаренко","Катерина Гриценко","Єлизавета Ткаченко"]

def making_groups(number):
    list_of_groups = []
    for i in range(number):
        list_of_groups.append([])

    temp = number
    index = 0
    while len(list_of_pupils)!=0:
        if number == 0:
            number = temp
        list_of_groups[number - 1].append(list_of_pupils[0])
        del(list_of_pupils[0])
        number -= 1
        index +=1

    for i in range(temp):
        print("group number",i+1,list_of_groups[i])


while True:
    try:
        max_number = len(list_of_pupils)//6+1
        min_number = len(list_of_pupils) // 18 + 1
        print("because number of pupils max number of group is:",max_number, "and minimal number is:",min_number)
        number_of_groups = int(input("Please, enter number of group which you want to make: "))
        if number_of_groups <= max_number and number_of_groups >= min_number:
            making_groups(number_of_groups)
            break

    except ValueError:
        print("Incorrect input")

