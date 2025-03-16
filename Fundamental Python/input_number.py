#Pada dasarnya syntax input() itu berupa tipe data String, Nah untuk bisa melakukan penjumlahan menggunakan input kita akan mengubahnya menjadi Integer/Angka
print("==Ini adalah contoh benar--")
print("Masukan Angka Pertama : ")
a = int(input())

print("Masukan Angka Kedua : ")
b = int(input())

hasil = a+b
print(F"Hasil dari {a} + {b} adalah {hasil}")

#Jika tidak menggunakan Int() maka syntax Input() akan dianggap sebagai String
#Contoh Salah
print(" ")
print("==Ini Adalah Contoh Salah==")
print("Masukan Angka Pertama : ")
a = input()

print("Masukan Angka Kedua : ")
b = input()

hasil = a+b
print(F"Hasil dari {a} + {b} adalah {hasil}")
