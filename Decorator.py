class Passenger:
    TITLES = ("Mr", "Mrs", "Ms")

    def __init__(self, title, fname, lname):
        if title not in self.TITLES:
            raise ValueError("%s is not a valid title." % title)
        
        self.title = title
        self.fname = fname
        self.lname = lname

p1 = Passenger ("Mr", "Mrs", "Ms")

print (p1.TITLES)
print (Passenger.TITLES)
print (p1.title)
print (Passenger.title)
# ----------------------------------------------
class Person:
    sehat = False

    def dinyatakan_sehat(self):
        self.sehat = True

joni = Person()
eko = Person()

joni.dinyatakan_sehat()
print("Joni sehat: ", joni.sehat)
print("Eko sehat: ", "eko.sehat")
# --------------------------------------------
def add_greeting(cls):
    def greeting(self):
        print(f"Hello, I am a {self.__class__.__name__}!")
    cls.greeting = greeting
    return cls

@add_greeting
class MyClass:
    pass
obj = MyClass()
obj.greeting()
# ------------------------------
def star(n):
    def decorate(fn):
        def wrapper(*args, **kwargs):
            print(n*'*')
            result = fn(*args, **kwargs)
            print(result)
            print(n*'*')
            return result
        return wrapper
    return decorate

@star(5)
def add(a, b):
    return a + b


add(10, 20)

