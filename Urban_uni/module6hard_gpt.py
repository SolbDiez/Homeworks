import math

class Figure:
    sides_count = 0

    def __init__(self, color, *sides):
        self.__color = list(color) if self.__is_valid_color(*color) else [0, 0, 0]
        self.filled = False
        if len(sides) != self.sides_count or not self.__is_valid_sides(*sides):
            self.__sides = [1] * self.sides_count
        else:
            self.__sides = list(sides)

    def __is_valid_color(self, r, g, b):
        return all(isinstance(value, int) and 0 <= value <= 255 for value in (r, g, b))

    def set_color(self, r, g, b):
        if self.__is_valid_color(r, g, b):
            self.__color = [r, g, b]

    def get_color(self):
        return self.__color

    def __is_valid_sides(self, *sides):
        return all(isinstance(side, int) and side > 0 for side in sides)

    def set_sides(self, *sides):
        if self.__is_valid_sides(*sides) and len(sides) == self.sides_count:
            self.__sides = list(sides)

    def get_sides(self):
        return self.__sides

    def __len__(self):
        return sum(self.__sides)


class Circle(Figure):
    sides_count = 1

    def __init__(self, color, *sides):
        super().__init__(color, *sides)
        self.__radius = self.get_sides()[0] / (2 * math.pi)

    def get_square(self):
        return math.pi * self.__radius ** 2

    def set_sides(self, *sides):
        if len(sides) == 1 and self._Figure__is_valid_sides(*sides):
            super().set_sides(*sides)
            self.__radius = self.get_sides()[0] / (2 * math.pi)


class Triangle(Figure):
    sides_count = 3

    def __init__(self, color, *sides):
        super().__init__(color, *sides)
        self.__height = None
        self.calculate_height()

    def calculate_height(self):
            a, b, c = self.get_sides()
            s = (a + b + c) / 2
            self.__height = (2 / a) * math.sqrt(s * (s - a) * (s - b) * (s - c))

    def get_square(self):
        a = self.get_sides()[0]
        return 0.5 * a * self.__height

    def set_sides(self, *sides):
        if len(sides) == 3 and self._Figure__is_valid_sides(*sides):
            super().set_sides(*sides)
            self.calculate_height()


class Cube(Figure):
    sides_count = 12

    def __init__(self, color, *sides):
        if len(sides) == 1:
            sides = [sides[0]] * self.sides_count
        super().__init__(color, *sides)
        self.__side_length = self.get_sides()[0]

    def get_volume(self):
        return self.__side_length ** 3

    def set_sides(self, *sides):
        if len(sides) == 1:
            sides = [sides[0]] * self.sides_count
        if self._Figure__is_valid_sides(*sides) and len(sides) == self.sides_count:
            super().set_sides(*sides)
            self.__side_length = self.get_sides()[0]


# Проверка реализации:
circle1 = Circle((200, 200, 100), 10)
cube1 = Cube((222, 35, 130), 6)

# Проверка на изменение цветов:
circle1.set_color(555, 66, 77)  # Изменится
cube1.set_color(300, 70, 15)  # Не изменится
print(circle1.get_color())  # Ожидается: [55, 66, 77]
print(cube1.get_color())  # Ожидается: [222, 35, 130]

# Проверка на изменение сторон:
cube1.set_sides(5, 3, 12, 4, 5)  # Не изменится
circle1.set_sides(15)  # Изменится
print(cube1.get_sides())  # Ожидается: [6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6]
print(circle1.get_sides())  # Ожидается: [15]

# Проверка периметра (круга), это и есть длина:
print(len(circle1))  # Ожидается: 15

# Проверка объёма (куба):
print(cube1.get_volume())  # Ожидается: 216
