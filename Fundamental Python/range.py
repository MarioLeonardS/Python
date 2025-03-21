# Tipe data Range
# Tipe data ini berfungsi untuk membatasi output range berupa angka
# Contohnya kita mau ngeprint angka dari 1-100
# Kita akan buat menjadi simple dan cepat
# Dalam fungsi "Range()" gunakan batas bawah dan batas atas, untuk print 1-100 batas atasnya ditambahkan 1

# Menggunakan Variable 
nomor = range(1, 101)

# Gunakan perintah For
for no in nomor:
    print(no)

# Hanya menggunakan perintah for untuk range
for no in range(1, 10001):
    print(no)