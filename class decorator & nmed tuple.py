'''
#Penyelesaian Soal 9.A
class Person:
    TITLES = ('Dr', 'Mr', 'Mrs', 'Ms')

    def __init__(self, name, surname):
        self.name = name
        self.surname = surname

    def fullname(self): # instance method
 # instance object accessible through self
        return "%s %s" % (self.name, self.surname)
    @property
    def fullname2(self):
        return "%s %s" % (self.name, self.surname)

    @classmethod
    def allowed_titles_starting_with(cls, startswith): # class method
 # class or instance object accessible through cls
        return [t for t in cls.TITLES if t.startswith(startswith)]
    @staticmethod
    def allowed_titles_ending_with(endswith): # static method
 # no parameter for class or instance object
 # we have to use Person directly
        return [t for t in Person.TITLES if t.endswith(endswith)]
    
jane = Person("Jane", "Smith")
print(jane.fullname())
print(jane.fullname2) # no brackets!
print(jane.allowed_titles_starting_with("M"))
print(Person.allowed_titles_starting_with("M"))
print(jane.allowed_titles_ending_with("s"))
print(Person.allowed_titles_ending_with("s"))

#No 2
class Tumbuhan: 
    jumlah_bunga = 5

    def __init__(self, nama_bunga):
        self.nama_bungan = nama_bunga
    
    @classmethod
    def panggil (cls):
        print (f'Bungan melati memliki {cls.jumlah_bunga}')

Tumbuhan.panggil()

class Konversi:
    @staticmethod
    def biner_decimal(x):
        decimal = int (x, 2)
        return decimal

bilangan_biner = Konversi.biner_decimal ("1011")
print (bilangan_biner)

class Kendaraan:
    def __init__ (self, kecepatan, waktu):
        self.kecepatan = kecepatan
        self.waktu = waktu

    @property
    def jarak (self):
        return self.kecepatan * self.waktu
    
jakarta = Kendaraan (80, 2)
print (jakarta.jarak)
print (f"jarak yang ditempuh adalah {jakarta.jarak} Km")

#Penyelesaian Soal 9.B
from collections import namedtuple
Koordinat = namedtuple ('koordinat', ['x', 'y'])
titik1 = Koordinat ('2', '4')
print ("Sumbu X:", titik1[0])
print ("Sumbu Y:", titik1.y)
print ('Sumbu X:', getattr(titik1, "x"))

from collections import namedtuple
Orang = namedtuple("Orang", "nama anak")
john = Orang("John Doe", ["Timmy", "Jimmy"])
print(john.x)
print(id(john.anak))
john.anak.append("Tina")
print(john)
print(id(john.anak))

def tampilkan_info(self):
    print("Nama : ", self.nama)
    print("Nama anak : ")
for i in range(len(self.anak)):
    print(f"{i+1}. {self.anak[i]}")

john.tampilkan_info()

from collections import namedtuple
jane = {"name": "Jane", "age": 25, "height": 1.75}
jane["age"] = 26
jane["age"]
jane["weight"] = 67
jane
# Equivalent named tuple
Person = namedtuple("Person", "name age height")
jane = Person("Jane", 25, 1.75)
jane
jane.age = 26
jane.weight = 67

from collections import namedtuple
Produk = namedtuple ("Produk", ["nama", "harga", "stok"])
produk1 = Produk (nama="buku tulis", harga=10000, stok=50)

def update_stok (produk, stok_tambahan):
    return produk._replace(stok=produk.stok + stok_tambahan)

produk1 = update_stok (produk1, 20)
print ("Nama:", produk1.nama)
print ("Harga:", produk1[2])
print ("Stok", getattr (produk1, "stok"))
'''