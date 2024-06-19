
def konversi_mil_ke_kilometer (mil):
    kilometer = mil * 1.60934
    return kilometer

mil = float(input("MASUKAN JUMLAH MIL YANG INGIN DI KONVERSI: "))
hasil_konversi = konversi_mil_ke_kilometer(mil)
print (f"{mil} mil = {hasil_konversi} kilometer")


from abc import ABC, abstractmethod

class Shape(ABC):                              
    @abstractmethod
    def area(self):
        pass

from abc import ABC, abstractmethod

# Abstract base class (inheritance and abstraction)
class Kendaraan (ABC):                         
    @abstractmethod
    def kecepatan (self):
        pass

# Polymorphism & inheritance yang mana menurunkan sifat dari induk class
class Mobil (Kendaraan):
    def __init__(self, jarak, waktu):
        self.jarak = jarak
        self.waktu = waktu

    def kecepatan (self):
        return self.jarak / self.waktu

class Motor (Kendaraan):
    def __init__(self, jarak, waktu):
        self.jarak = jarak
        self.waktu = waktu

    def kecepatan (self):
        return self.jarak / self.waktu

def hitung_kecepatan(Kendaraan):
    return Kendaraan.kecepatan()

Avanza = Mobil (100, 20)
Supra = Motor (80, 20)

print (f"Kecepatan: {hitung_kecepatan(Avanza)} Km/h")
print (f"Kecepatan: {hitung_kecepatan(Supra)} Km/h")

class Rekening:
    def __init__(self, nama, no_rekening, saldo):
        self.nama = nama
        self.no_rekening = no_rekening
        self.saldo = saldo
        
class Nasabah (Rekening):
    
    def menampilkan_data (self):
        print ("Nama: ", self.nama)
        print ("No_Rekening: ", self.no_rekening)
        print ("Saldo: ", self.saldo)

nasabah_1 = Nasabah ("Budi", 5555, 500000)
nasabah_2 = Nasabah ("Wati", 6666, 2000000)

print ("Nasabah 1")
nasabah_1.menampilkan_data()
print ("\nNasabah 2")
nasabah_2.menampilkan_data()

