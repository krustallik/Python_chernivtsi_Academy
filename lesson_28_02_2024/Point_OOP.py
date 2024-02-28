class Point:
    # Статична змінна для відстеження кількості створених точок
    points_count = 0

    def __init__(self, x=0, y=0, based_on=None):
        # Якщо надано точку, на основі якої треба створити нову з протилежними координатами
        if based_on is not None:
            self.x = -based_on.x
            self.y = -based_on.y
        else:
            self.x = x
            self.y = y
        Point.points_count += 1  # Інкрементуємо лічильник створених точок

    def enter_data(self):
        try:
            self.x = float(input("Введіть координату x: "))
            self.y = float(input("Введіть координату y: "))
        except ValueError:
            print("Incorrect Value")


    def display_data(self):
        print(f"Координати точки: ({self.x}, {self.y})")

    def edit_data(self, x=None, y=None):
        if x is not None:
            self.x = x
        if y is not None:
            self.y = y

    @classmethod
    def get_points_count(cls):
        print(f"Загальна кількість створених точок: {cls.points_count}")

# Приклади використання
point1 = Point(1, 2)
point1.display_data()

point2 = Point(based_on=point1)
point2.display_data()

Point.get_points_count()

point1.enter_data()
point1.display_data()

point1.edit_data(x=10)
point1.display_data()

Point.get_points_count()
