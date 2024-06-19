class Rekening:
    def __init__(self, nama, no_rekening, saldo):
        self.nama = nama
        self.no_rekening = no_rekening
        self.saldo = saldo

    def setor_tunai (self, saldo_baru):
        self.saldo += saldo_baru
        return self.saldo
    
    def tarik_tunai (self, tarik_saldo):
        self.saldo -= tarik_saldo
        return self.saldo
    
    def transfer (self, jumlah, penerima):
        self.saldo -= jumlah
        penerima.saldo += jumlah
        print (f"\nTransfer sebesar 500000 dari rekening {self.nama} ke rekening {penerima.nama} berhasil")

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

nasabah_1.setor_tunai(1000000)
nasabah_2.tarik_tunai(1000000)

print ("\nTransaksi Update")
print ("Saldo Nasabah 1 Setelah setor tunai: ", nasabah_1.saldo)
print ("Saldo Nasabah 2 Setelah setor tunai: ", nasabah_2.saldo)

nasabah_1.transfer (500000, nasabah_2)

print ("Jumlah saldo Nasabah 1 setelah melakukan transfer", nasabah_1.saldo)
print ("Jumlah saldo Nasabah 2 setelah menerima transfer", nasabah_2.saldo)