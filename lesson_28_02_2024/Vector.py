import random
import time
class Vector:
    def __init__(self):
        self.vector = [random.randint(10, 99) for _ in range(12)]

    def display_vector(self):
        for i in range(0, 12, 3):
            print(f'{self.vector[i]} {self.vector[i+1]} {self.vector[i+2]}')
        time.sleep(5)
        print('\n' * 100)

    def fill_vector(self):
        self.vector = [int(input(f"Введіть елемент {i+1}/12: ")) for i in range(12)]

    def compare_vectors(self, other):
        return sum(a == b for a, b in zip(self.vector, other.vector))

# Головна програма
print("Спробуйте запам'ятати якомога більше чисел з наступного списку:")
vector1 = Vector()
vector1.display_vector()

print("Час вийшов! Тепер введіть числа, які ви запам'ятали.")
vector2 = Vector()
vector2.fill_vector()

correct_count = vector1.compare_vectors(vector2)
print(f"Ви правильно згадали {correct_count} чисел з 12.")
