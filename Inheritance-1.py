#XxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxX#
class Person(object):
    def __init__(self, name):
        self.name = name

    def getName(self):
        return self.name

    def isEmployee(self):
        return False

class Employee(Person):
    def isEmployee(self):
        return True

emp = Person ("Slamet")
print(emp.getName(), emp.isEmployee())

emp = Employee("Santoso")
print(emp.getName(), emp.isEmployee())
#XxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxX#
class Shape:
    width = 0
    def __init__(self, width):
        self.width = width

class Square (Shape):
    name = "Square"
    def get_area(self):
        print (self.width ** 2)

class Triangle(Shape):
    name = "Triangle"
    height = 0
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def get_area(self):
        print (0.5 * self.width * self.height)

SquareX = Square(5)
TriangleY = Triangle(5, 3)

SquareX.get_area()
TriangleY.get_area()
#XxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxX#
class Koordinator2D: 
    x = 0
    y = 0

    def __init__(self, x, y):
        self.x = x
        self.y = y

class Koordinator3D(Koordinator2D):
    z = 0

    def __init__(self,x,y,z):
        super().__init__(x,y)
        self.z = z

    def tampilkan_koord(self):
        print("x = ", self.x)
        print("y = ", self.y)
        print("z = ", self.z)

titik1 = Koordinator3D(1,2,3)
titik1.tampilkan_koord()

delattr(titik1, 'z')
print('efek fungsi delattr()')
titik1.tampilkan_koord()

del titik1.y
print('efek keyword del')
titik1.tampilkan_koord()

del Koordinator2D.y
del titik1.y
print('efek keyword del')
titik1.tampilkan_koord()
#XxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxX#
class Bird:

    def __init__(self):
        print("Bird is ready")

    def whoisThis(self):
        print("Bird")

    def swim(self):
        print("Swim faster")    

class Penguin(Bird):

    def __init__(self):
        super().__init__()
        print("Penguin is ready")

    def whoisThis(self):
        print("Penguin")

    def run(self):
        print("Run faster")

peggy = Penguin()
peggy.whoisThis()
peggy.swim()
peggy.run()
#XxxxxxxxxxxxxxxxxxxxxxxxxxX#
class Contoh:
    def __init__(self, nilai):
        self.nilai = nilai

objek = Contoh(10)
print(objek.nilai)  

del objek.nilai
print(objek.nilai)  
#XxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxX#
class Kelas:
    def __init__(self, nama):
        self.nama = nama

objek = Kelas("Faisal")
print(objek.nama)  

del objek.nama
print(objek.nama)  