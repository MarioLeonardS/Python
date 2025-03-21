# Belajar IF-Statement
# Untuk penggunaanya harus ada kondisi, aksi, dll
# Saat menggunakan if-statement, setelah kondisi harus diberikan Tab untuk codenya bisa dieksekusi
# Saat menjalankan code yang berisi banyak statement IF, maka semua statement IF akan dieksekusi
# if kondisi:
    # melakukan apa?
    # melakukan hal lain
    # dan seterusnya

# Contoh penggunaan
# Buat Kondisi Jika dapat nilai bagus, jelek, biasa aja
print("== Hasil Ujian Matematika Kelas 11 TJKT 2 ==")
print(" ")
print("Masukan Nilai Matematika")
nilai = int(input("Nilai : "))
kkm = 75

if nilai > kkm:
    print("Wih! Diatas KKM")

if nilai < kkm:
    print("Yaelah, remedial dong")

if nilai == kkm:
    print("Yaudahlah, yang penting pas KKM")

if nilai == 100:
    print("Sempurna!")