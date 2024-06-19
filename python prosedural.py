#soal 1
angka = int(input("Masukan Angka:"))
for i in range(angka, -1, -1):
    print(i, end=" ")
#soal 2
suhu = float(input("Masukan Suhu: "))
if suhu < 0:
    print("Membeku")
elif suhu < 10:
    print("Sangat Dingin")
elif suhu < 20:
    print("Sejuk")
elif suhu < 30:
    print("Hangat")
elif suhu < 40:
    print("Panas")
else:
    print("Sangat Panas")
#soal 3
NIU = int(input("Masukan NIU Anda: "))
Tugas = float(input("Masukan Nilai Tugas Anda: "))
Laporan = float(input("Masukan Nilai Laporan Anda: "))
rata_rata = (Tugas + Laporan)/2
if rata_rata < 40:
    print("Siswa memperoleh Nilai K karena memiliki nilai kurang dari 40")
else:
    Ujian = float(input("Masukan Nilai Ujian Kamu: "))
    bobot_rata_rata = 0.25
    bobot_ujian = 0.5
    nilai_akhir = (bobot_rata_rata * rata_rata) + (bobot_ujian * Ujian)
    if nilai_akhir >= 80:
        nilai = "A"
    elif nilai_akhir >= 70:
        nilai = "B"
    elif nilai_akhir >= 60:
        nilai = "C"
    elif nilai_akhir >= 50:
        nilai = "D"
    else:
        nilai = "E"
    print(f"Nilai akhir siswa dengan NIU {NIU}: {nilai_akhir:.2f} (Nilai Huruf: {nilai})")
#soal 4
bilangan = int(input("Masukkan angka: "))
if bilangan > 1:
    for i in range(2, int(bilangan/2) + 1):
        if (bilangan % i) == 0:
            print(f"{bilangan} bukan angka prima.")
            break
    else:
        print(f"{bilangan} adalah angka prima.")
else:
    print(f"{bilangan} bukan angka prima.")
#soal 5
import math
jari_jari = int(input("Masukan Jari Jari: "))
luas = math.pi * jari_jari ** 2
keliling = 2 * math.pi * jari_jari
print("luas lingkaran :", luas)
print("keliling lingkaran :", keliling)