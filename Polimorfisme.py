class TV:
    def menyala(self):
        print ("menyakan Televisi")

class AC:
    def menyala (self):
        print ("menyakan Air Conditioner")

tipi = TV()
ace = AC()

tipi.menyala()
ace.menyala()

#-------------------------------------------

class Barang: 
    def __init__(self, merek, harga_satuan):
        self.merek = merek
        self.harga_satuan = harga_satuan

    def __mul__ (self, kuantitas):
        print ("Banyaknya Penjualan: ", kuantitas.qty_jual, "buah")
        return self.harga_satuan * kuantitas.qty_jual
    
class Penjualan:
    def __init__ (self, merek, qty_jual):
        self.merek = merek
        self.qty_jual = qty_jual

redmi10 = Barang ("Redmi10", 2140)
qty_maret = Penjualan ("Redmi10", 20)
print (f"Total Penjualan redmi10: {redmi10*qty_maret} Ribu")
 
#-------------------------------------------

class Kendaraan:
    def __init__ (self, nama):
        self.nama = nama

    def kecepatan (self):
        print ("kecepatan Kendaraan")

class Motor (Kendaraan):
    def kecepatan(self):
        super (Motor, self).kecepatan()
        return "70 km/h"
    
class Mobil (Kendaraan):
    def kecepatan(self):
        Kendaraan.kecepatan(self)
        return "100 km/h"
    
class Kereta (Kendaraan):
    def kecepatan(self):
        Kendaraan.kecepatan(self)
        return "150 km/h"
    
class Pesawat (Kendaraan):
    def kecepatan(self):
        Kendaraan.kecepatan(self)
        return "200 km/h"
    
motorcycle = Motor ("Motor")
car = Mobil ("Mobil")
thomas = Kereta ("Kereta")
lion = Pesawat ("Pesawat")

print ("Kecepatan", motorcycle.nama, "yaitu", motorcycle.kecepatan())
print ("Kecepatan", car.nama, "yaitu", car.kecepatan())
print ("Kecepatan", thomas.nama, "yaitu", thomas.kecepatan())
print ('Kecepatan', lion.nama, 'yaitu', lion.kecepatan())

#------------------------------------------------------


class Sekolah: 
    def __init__(self, nama, laki_laki):
        self.nama = nama
        self.laki_laki = laki_laki

    def __add__ (self, x):
        print ("Banyaknya Siswa Laki Laki: ", self.laki_laki, "orang")
        return self.laki_laki + x.perempuan
    
class Anak_Perempuan:
    def __init__ (self, nama, perempuan):
        self.nama = nama
        self.perempuan = perempuan

UGM = Sekolah ("UGM", 100)
UGM_PR = Anak_Perempuan ("UGM", 200)
print (f"Total Murid di UGM: {UGM.nama}: {UGM + UGM_PR} orang")


