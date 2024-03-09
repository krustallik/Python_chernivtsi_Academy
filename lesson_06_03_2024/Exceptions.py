class TernaryNumberError(Exception):
    def __init__(self, message='Помилка у тернарній арифметиці'):
        super().__init__(message)

class TernaryNumber:
    def __init__(self, number):
        self.validate(number)
        self.number = number

    @staticmethod
    def validate(number):
        if number not in [0, 1, 2]:
            raise TernaryNumberError(f"Невідоме число: {number}")

    @staticmethod
    def add(a, b):
        if a == b == 0:
            return 0
        elif a == b == 1:
            return 2
        elif (a == 1 and b == 0) or (a == 0 and b == 1):
            return 1
        else:
            return 10

try:
    num1 = TernaryNumber(3)
    num2 = TernaryNumber(1)
    print("Результат:", TernaryNumber.add(num1.number, num2.number))
except TernaryNumberError as e:
    print(e)
