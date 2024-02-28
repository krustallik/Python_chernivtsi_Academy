def gcd(a, b):
    """Знаходження найбільшого спільного дільника (НСД) для скорочення дробу."""
    while b:
        a, b = b, a % b
    return a

class Fraction:
    def __init__(self, numerator, denominator):
        self.numerator = numerator
        self.denominator = denominator
        self.reduce()

    def reduce(self):
        """Скорочення дробу."""
        greatest_common_divisor = gcd(self.numerator, self.denominator)
        self.numerator //= greatest_common_divisor
        self.denominator //= greatest_common_divisor

    def __str__(self):
        """Повертає рядкове представлення дробу."""
        return f"{self.numerator}/{self.denominator}"

    def __add__(self, other):
        """Додавання двох дробів."""
        new_numerator = self.numerator * other.denominator + self.denominator * other.numerator
        new_denominator = self.denominator * other.denominator
        return Fraction(new_numerator, new_denominator)

    def __sub__(self, other):
        """Віднімання двох дробів."""
        new_numerator = self.numerator * other.denominator - self.denominator * other.numerator
        new_denominator = self.denominator * other.denominator
        return Fraction(new_numerator, new_denominator)

    def __mul__(self, other):
        """Множення двох дробів."""
        new_numerator = self.numerator * other.numerator
        new_denominator = self.denominator * other.denominator
        return Fraction(new_numerator, new_denominator)

    def __truediv__(self, other):
        """Ділення двох дробів."""
        new_numerator = self.numerator * other.denominator
        new_denominator = self.denominator * other.numerator
        return Fraction(new_numerator, new_denominator)


# Створення дробів
fraction1 = Fraction(1, 2)
fraction2 = Fraction(3, 4)

# Додавання дробів
addition = fraction1 + fraction2
print(f"Додавання: {fraction1} + {fraction2} = {addition}")

# Віднімання дробів
subtraction = fraction1 - fraction2
print(f"Віднімання: {fraction1} - {fraction2} = {subtraction}")

# Множення дробів
multiplication = fraction1 * fraction2
print(f"Множення: {fraction1} * {fraction2} = {multiplication}")

# Ділення дробів
division = fraction1 / fraction2
print(f"Ділення: {fraction1} / {fraction2} = {division}")
