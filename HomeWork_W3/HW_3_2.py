class Point2D:

    __count = 0

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.__class__.__count += 1

    def distance(self, other):
        return ((self.x - other.x) ** 2 + (self.y - other.y) ** 2) ** 0.5

    @property
    def count(self):
        return self.__count

    @count.setter
    def count(self, count):
        self.__count = count


class Point3D(Point2D):
    def __init__(self, x, y, z):
        super().__init__(x, y)
        self.z = z

    def distance(self, other):
        return ((self.x - other.x) ** 2 + (self.y - other.y) ** 2 + + (self.z - other.z) ** 2) ** 0.5


p1 = Point2D(-1, 3)
p2 = Point2D(6, 2)

p3 = Point3D(-1, 3, 3)
p4 = Point3D(6, 2, -2)

print('Distance: ', p1.distance(p2))
print('Count points:', p2.count)
print()
print('Distance: ', p3.distance(p4))
print('Count points:', p4.count)

# Створити клас Point2D. Координати точки задаються 2 параметрами – координатами x, y на площині.
#
# Реалізувати метод distance який приймає екземпляр класу Point2D та розраховує відстань між двома точками на площині.
#
# Створити захищений атрибут класу – лічильник створених екземплярів класу.
#
# Читання кількості екземплярів реалізувати через метод getter.
#
# Створити клас Point3D, який є спадкоємцем класу Point2D.
# Координати точки задаються 3 параметрами – координатами x, y, z у просторі.
#
# Перевизначити конструктор за допомогою super().
#
# Перевизначити метод distance для визначення відстані між двома точками у просторі.
