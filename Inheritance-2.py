class Orang:

    def __init__(self, nama_depan, nama_belakang, id):
        self.nama_depan = nama_depan
        self.nama_belakang = nama_belakang
        self.id = id

    def tampilkan_nama(self):
        print("Nama Depan: " + self.nama_depan)
        print("Nama Belakang: " + self.nama_belakang)
        print("ID: " + str(self.id))

class Mahasiswa (Orang):
    SARJANA, MAGISTER, DOKTOR = range(3)

    def __init__(self, nama_depan, nama_belakang, id, jenjang):
        super().__init__(nama_depan, nama_belakang, id)
        self.jenjang = jenjang
        self.matkul = []
        if jenjang < 1: 
            self.jenjang = "sarjana"
        elif jenjang < 2:
            self.jenjang = "magister"
        else:
            self.jenjang = "Doktor"

    def enroll(self, mata_kuliah):
        self.matkul.append(mata_kuliah)
    
    def tampilkan_nama(self):
        print("Nama Depan: " + self.nama_depan)
        print("Nama Belakang: " + self.nama_belakang)
        print("ID: " + str(self.id))
        print("Status: ", self.jenjang)
        print("Mata Kuliah yang diambil: ", self.matkul)

class Karyawan (Orang):
    Tetap, Tidak_tetap = range(2)

    def __init__(self, nama_depan, nama_belakang, id, status):
        super().__init__(nama_depan, nama_belakang, id)
        self.status = status

class Dosen (Orang): 
    Tetap, Tidak_Tetap = range(2)

    def __init__(self, nama_depan, nama_belakang, id, status):
        super().__init__(nama_depan, nama_belakang, id)
        self.status = status
        self.matkuldiajar = []
        if status < 1: 
            self.status = "Tetap"
        else:
            self.status = "Tidak Tetap"

    def mengajar(self, matakuliahdosen):
        self.matkuldiajar.append(matakuliahdosen)

    def tampilkan_nama(self):
        print("Nama Depan: " + self.nama_depan)
        print("Nama Belakang: " + self.nama_belakang)
        print("ID: " + str(self.id))
        print("Status: ", self.status)
        print("Matkul yang diajar: ", self.matkuldiajar)

bowo = Mahasiswa ("Bowo", "Apenlibe", 987654, Mahasiswa.SARJANA)
bowo.enroll ("Basis Data")

rizky = Dosen ("Rizky", "Setiabudi", 456789, Dosen.Tetap)
rizky.mengajar ("statistika")

bowo.tampilkan_nama()
rizky.tampilkan_nama()

class Pelajar:
    def __init__(self):
        self.matkul = []

    def enrol(self, mata_kuliah):
        self.matkul.append(mata_kuliah)

class Pengajar:
    def __init__(self):
        self.matkul_diajar = []

    def mengajar(self, mata_kuliah):
        self.matkul_diajar.append(mata_kuliah)

class Asdos (Orang, Pelajar, Pengajar):
    def __init__(self, nama_depan, nama_belakang, id):
        Orang.__init__(self, nama_depan, nama_belakang, id)
        Pelajar.__init__(self)
        Pengajar.__init__(self)

uswatun = Asdos ("Uswatun", "Hasanah", 456456)
uswatun.enrol("Big Data")
uswatun.mengajar("Kecerdasan Artifisial")

print ("Identitas Uswatun:")
uswatun.tampilkan_nama()
print ("Mata Kuliah yang diambil:", uswatun.matkul)
print ("Mata Kuliah yang diajar:", uswatun.matkul_diajar)






